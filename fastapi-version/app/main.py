from cassandra.cluster import Session
from fastapi import FastAPI, Depends, HTTPException, Request
from pydantic import validators
from redis import Redis
from starlette.responses import RedirectResponse

from app import schemas
from app.controller import UrlShortener
from app.database import get_redis_client, get_cassandra_session

app = FastAPI()


def raise_bad_request(message: str):
    raise HTTPException(status_code=400, detail=message)


def raise_not_found(request: Request):
    message = f"URL '{request.url}' doesn't exist"
    raise HTTPException(status_code=404, detail=message)


@app.post("/url", response_model=schemas.UrlShorted)
def create_url(
    urlschema: schemas.URLBase,
    db_session: Session = Depends(get_cassandra_session),
    redis_client: Redis = Depends(get_redis_client),
):
    if not validators.url(urlschema.url):
        raise_bad_request(message="Your provided URL is not valid")
    shorted_url = UrlShortener(db_session=db_session, redis_client=redis_client).create_url(url=urlschema.url)
    return shorted_url


@app.get("/{url_key}")
def forward_to_target_url(
    url_key: str,
    request: Request,
    db_session: Session = Depends(get_cassandra_session),
    redis_client: Redis = Depends(get_redis_client),
):
    shorted_url = UrlShortener(db_session=db_session, redis_client=redis_client).get_url(url_key)

    if shorted_url:
        return RedirectResponse(shorted_url)
    else:
        raise_not_found(request)
