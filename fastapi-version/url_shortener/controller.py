import logging
from functools import lru_cache
from typing import Optional

from cassandra.cluster import Session
from fastapi import Depends
from redis import Redis

from url_shortener.database import get_cassandra_session, get_redis_client
from url_shortener.models import URLModel
from url_shortener.schemas import UrlShorted
from url_shortener.utils import create_random_key

logger = logging.getLogger(__name__)


class UrlShortener:
    """class for controlling shortening URLs functionality"""
    cache_ttl = 60 * 60 * 2

    def __init__(
        self, db_session: Session = Depends(get_cassandra_session), redis_client: Redis = Depends(get_redis_client)
    ) -> None:
        super().__init__()
        self.db_session = db_session
        self.url_model = URLModel(db_session=db_session)
        self.redis_client = redis_client

    def _persist_url_in_db(self, url: str, shorted_url: str):
        self.url_model.create_url(url, shorted_url)

    def _get_url_from_db(self, url: str) -> Optional[str]:
        return self.url_model.get_url(url)

    def _get_url_from_cache(self, shorted_url: str) -> Optional[str]:
        return self.redis_client.get(shorted_url)

    def _get_shorted_url_and_update_expired(self, shorted_url: str) -> Optional[str]:
        if url := self._get_url_from_cache(shorted_url):
            self._update_shortened_url_expired_cache(shorted_url)
            return url
        return None

    def _update_shortened_url_expired_cache(self, shorted_url: str):
        """update expired cache for shorted url"""
        self.redis_client.expire(shorted_url, time=self.cache_ttl)

    def _set_url_in_cache(self, url: str, shorted_url: str):
        self.redis_client.set(shorted_url, url, ex=3600)

    def create_url(self, url: str) -> UrlShorted:
        """create new shorted url and set it to redis for future data access"""
        shorted_url = create_random_key(length=5)
        self._persist_url_in_db(url, shorted_url)
        self._set_url_in_cache(url, shorted_url)
        return UrlShorted(shorted_url=shorted_url, url=url)

    @lru_cache(maxsize=10_000)
    def get_url(self, shorted_url: str) -> str:
        """get url based on given shorted url,
            I used lru cache for frequently accessed URLs
            then if not set in lru try to get it from redis
            at the end if we cant find the shorted url, we try to get it from db
        """
        if url := self._get_shorted_url_and_update_expired(shorted_url):
            return url

        url = self._get_url_from_db(shorted_url)
        try:
            self._set_url_in_cache(url, shorted_url)
        except Exception:
            # for more robustness
            logger.exception(e)
        return url
