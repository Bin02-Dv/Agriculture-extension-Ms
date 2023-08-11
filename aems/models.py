from django.db import models

# Create your models here.


class Officer(models.Model):
    full_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=100, blank=True)
    contact_address = models.TextField(max_length=100, blank=True)
    extention = models.CharField(max_length=100, blank=True)
    farm = models.CharField(max_length=50, blank=True)
    date_visit = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.full_name


class Farmers(models.Model):
    full_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=100, blank=True)
    contact_address = models.TextField(max_length=100, blank=True)
    extention = models.CharField(max_length=100, blank=True)
    farm = models.CharField(max_length=50, blank=True)
    date_visit = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.full_name

class FarmDetails(models.Model):
    farm_location = models.CharField(max_length=100, blank=True)
    farm_size = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.farm_location

class Visit_history(models.Model):
    full_name = models.CharField(max_length=100, blank=True)
    date_visit = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.full_name
