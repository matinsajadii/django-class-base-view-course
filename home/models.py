from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    created = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name