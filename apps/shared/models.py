from enum import Enum
from django.db import models
from apps.flax_id.django.fields import FlaxId


class BaseEnum(Enum):
    @property
    def display_name(self):
        return self.name.replace("_", " ").title()

    def __str__(self):
        return str(self.value)

    @classmethod
    def choices(cls):
        return [
            (str(value), key.replace("_", " ").title())
            for key, value in cls.__members__.items()
        ]

    @classmethod
    def slugs(cls):
        return cls.__members__.values()


class BaseModel(models.Model):
    id = FlaxId(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
