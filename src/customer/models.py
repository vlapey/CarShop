from django.db import models
from core.abstract_models import ModelProperties
from core.enums import IsHavingLicense


class Customer(ModelProperties):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField
    balance = models.PositiveIntegerField(default=0)
    is_having_license = models.CharField(max_length=3, choices=IsHavingLicense.choices(), default='n')

    def __str__(self):
        return self.name
