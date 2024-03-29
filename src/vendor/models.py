from django.db import models
from core.abstract_models import ModelProperties


class Vendor(ModelProperties):
    name = models.CharField(max_length=30, unique=True)
    foundation_year = models.CharField(max_length=4)
    buyers_amount = models.PositiveIntegerField(default=0)
