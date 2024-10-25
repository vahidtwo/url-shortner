from django.db import models


class CreatedAtColumnMixin:
    created_at = models.DateTimeField(auto_now_add=True)


class BaseModel(CreatedAtColumnMixin, models.Model):
    class Meta:
        abstract = True
