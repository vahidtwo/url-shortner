from unittest import TestCase

from starlette.testclient import TestClient

from url_shortener.app import fastapi_app
from url_shortener.database import get_cassandra_session, get_redis_client

"""
I dont have enough time to implement tests sorry 🙃
"""
client = TestClient(fastapi_app)


def redis_mock(*args, **kwargs):
    pass


def cassandra_mock(*args, **kwargs):
    pass


fastapi_app.dependency_overrides = dict()
fastapi_app.dependency_overrides[get_cassandra_session] = cassandra_mock
fastapi_app.dependency_overrides[get_redis_client] = redis_mock


class ControllerTests(TestCase):
    def test_get_from_cache(self):
        pass

    def test_set_to_cache(self):
        pass

    def test_create_url(self):
        # mock inner function call
        # check which each function call with their parameter
        pass

    def test_get_url(self):
        # mock inner function call
        # check which each function call with their parameter
        pass

    # etc


class ViewTestCase(TestCase):
    def test_get_url(self):
        pass

    def test_set_url(self):
        pass


class UtilsTestCase(TestCase):
    def test_get_random_number(self):
        pass
