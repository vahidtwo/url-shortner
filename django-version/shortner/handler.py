import logging
import random
import string
from functools import lru_cache
from typing import Optional

from shortner.models import ShortUrl
from utils.redis import redis_client

logger = logging.getLogger(__name__)


class UrlShortenerHandler:
    cache_ttl = 60 * 60 * 2

    @staticmethod
    def _persist_url_in_db(url: str, shorted_url: str) -> ShortUrl:
        return ShortUrl.objects.create(
            url=url,
            url_shortened=shorted_url,
        )

    @staticmethod
    def _get_url_from_db(url: str) -> Optional[str]:
        try:
            return ShortUrl.objects.get(url_shortened=url).url
        except ShortUrl.DoesNotExist:
            return None

    @staticmethod
    def _get_url_from_cache(shorted_url: str) -> Optional[str]:
        return redis_client.get(shorted_url)

    @classmethod
    def _get_shorted_url_and_update_expired(cls, shorted_url: str) -> Optional[str]:
        if url := cls._get_url_from_cache(shorted_url):
            cls._update_shortened_url_expired_cache(shorted_url)
            return url
        return None

    @classmethod
    def _update_shortened_url_expired_cache(cls, shorted_url: str):
        """update expired cache for shorted url"""
        redis_client.expire(shorted_url, expire=cls.cache_ttl)

    @staticmethod
    def _set_url_in_cache(url: str, shorted_url: str):
        redis_client.set(shorted_url, url, ex=3600)

    @classmethod
    def create_url(cls, url: str) -> ShortUrl:
        shorted_url = random.choices(string.ascii_letters + string.digits, k=5)
        db_object = cls._persist_url_in_db(url, shorted_url)
        cls._set_url_in_cache(url, shorted_url)
        return db_object

    @classmethod
    @lru_cache(maxsize=10_000)
    def get_url(cls, shorted_url: str) -> str:
        if url := cls._get_shorted_url_and_update_expired(shorted_url):
            return url

        url = cls._get_url_from_db(shorted_url)
        try:
            cls._set_url_in_cache(url, shorted_url)
        except Exception:
            # for more robustness
            logger.exception(f"failed to set url {shorted_url}")
        return url
