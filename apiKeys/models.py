from django.contrib.auth.models import User
from django.db import models


class ApiKey(models.Model):
    key = models.CharField(max_length=80)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.key + ', ' + str(self.is_active)
