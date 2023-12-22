from django.db import models
from core.abstract_models import ModelProperties


class Customer(ModelProperties):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.name
