import uuid
from django.db import models


class Cities(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    division_type = models.TextField(max_length=50, blank=True)
    name = models.TextField(max_length=50)
    image_url = models.ImageField(upload_to='assets/location')
    position = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(max_length=50)
    image_url = models.ImageField(upload_to='assets/car_type')
    position = models.IntegerField(default=1)

    def __str__(self):
        return self.name
