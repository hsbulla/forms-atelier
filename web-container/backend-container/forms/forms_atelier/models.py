from django.db import models

class data(models.Model):
    manager = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    middleName = models.CharField(max_length=100)
    measurements = models.CharField(max_length=100)
    fabricType = models.CharField(max_length=100)
    deliveryOption = models.CharField(max_length=100)