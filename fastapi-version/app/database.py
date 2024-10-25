from cassandra.cluster import Cluster, Session
from fastapi import Depends
from redis import Redis

from app.configs import Settings


def get_cassandra_session(settings: Settings = Depends(Settings)) -> Session:
    cassandra_cluster = Cluster([settings.cassandra_url])
    cassandra_session = cassandra_cluster.connect("url_shortener")
    try:
        yield cassandra_session
    finally:
        cassandra_session.shutdown()


def get_redis_client(settings: Settings = Depends(Settings)) -> Redis:
    redis_client = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, password=settings.REDIS_PASSWORD)
    yield redis_client
