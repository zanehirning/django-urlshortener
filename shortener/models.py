from django.db import models


class Url(models.Model):
    link = models.URLField(max_length=10000)
    uuid = models.CharField(max_length=10)

    def __str__(self):
        return self.uuid
# Create your models here.
