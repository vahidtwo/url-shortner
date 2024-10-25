from redis import Redis
from django.conf import settings

redis_client = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, password=settings.REDIS_PASSWORD)
