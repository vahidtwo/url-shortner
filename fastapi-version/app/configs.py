from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379
    CASSANDRA_CLUSTER_NAME: str = "test"
    CASSANDRA_USER: str = "cassandra"
    CASSANDRA_PASSWORD: str = "cassandra"

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings
