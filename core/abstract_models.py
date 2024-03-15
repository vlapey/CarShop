from django.db import models


class ModelProperties(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(blank=True, auto_now_add=True)

    class Meta:
        abstract = True
