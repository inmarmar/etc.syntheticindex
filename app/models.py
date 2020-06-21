from django.db import models
from django.utils import timezone

class Price(models.Model):
    price = models.FloatField()
    date = models.DateField(null = False, default = timezone.now, db_index=True)
    weight = models.FloatField()

    def __str__(self):
        return '{}'.format(self.price)
