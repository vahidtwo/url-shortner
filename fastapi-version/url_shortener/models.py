from cassandra.cluster import Session
from cassandra.query import SimpleStatement
from fastapi import Depends

from url_shortener.database import get_cassandra_session


class URLModel:
    def __init__(self, db_session: Session = Depends(get_cassandra_session)):
        self.db_session = db_session

    def create_url(self, short_url: str, url: str) -> str:
        query = "INSERT INTO urls (short_url, url) VALUES (%s, %s)"
        return self.db_session.execute(SimpleStatement(query), (short_url, url))

    def get_url(self, short_url: str) -> str:
        query = "SELECT url FROM urls WHERE short_url=%s"
        result = self.db_session.execute(SimpleStatement(query), (short_url,))
        return result.one().url
