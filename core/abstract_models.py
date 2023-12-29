from django.db import models


class ModelProperties(models.Model):
    is_active = models.BooleanField(default=True)
    time_created = models.DateTimeField(auto_now=True)
    time_updated = models.DateTimeField(blank=True, auto_now_add=True)

    class Meta:
        abstract = True
