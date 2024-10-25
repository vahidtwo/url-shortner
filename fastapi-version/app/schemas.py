from pydantic import BaseModel, Field, ConfigDict


class URLBase(BaseModel):
    url: str
    model_config = ConfigDict(from_attributes=True)


class UrlShorted(URLBase):
    shorted_url: str
