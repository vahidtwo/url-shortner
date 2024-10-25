from cassandra.cluster import Cluster, Session
from fastapi import Depends
from redis import Redis

from configs import Settings, get_settings


def get_cassandra_session(settings: Settings = Depends(get_settings)) -> Session:
    cassandra_cluster = Cluster([settings.CASSANDRA_URL])
    cassandra_session = cassandra_cluster.connect("url_shortener")
    try:
        yield cassandra_session
    finally:
        cassandra_session.shutdown()


def get_redis_client(settings: Settings = Depends(get_settings)) -> Redis:
    redis_client = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, password=settings.REDIS_PASSWORD)
    yield redis_client
