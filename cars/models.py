from django.db import models


class Car(models.Model):
    car_name = models.CharField(max_length=100)
    model = models.TextField()
    year = models.DecimalField(max_digits=40, decimal_places=5)

