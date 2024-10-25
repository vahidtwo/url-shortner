from django.db import models

from commons.models.base import BaseModel


class ShortUrl(BaseModel):
    url = models.TextField()  # not set unique for db not lock for unique check
    shorted_url = models.CharField(max_length=5, unique=True, db_index=True)
