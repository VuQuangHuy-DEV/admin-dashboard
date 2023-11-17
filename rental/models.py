import uuid
from functools import partial

from django.db import models
from authentication.models import User

from general.models import Vehicle
from ultis.helper import custom_user_image_path


class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(max_length=150)

    def __str__(self):
        return self.name


class Model(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(max_length=150)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class RentalPost(models.Model):
    custom_image_path = partial(custom_user_image_path, path="rental")

    STATUS_CHOICES = (
        ('rent', 'Đang cho thuê'),
        ('ready', 'Sẵn sàng'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(null=False, max_length=200)
    details = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ready")
    brand = models.CharField(null=False, blank=False, max_length=100)
    model = models.CharField(null=False, blank=False, max_length=100)
    license_plate = models.CharField(null=False, blank=False, max_length=20)
    location = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    num_of_people = models.PositiveIntegerField()
    allows_pet = models.BooleanField()
    sub_service = models.CharField(max_length=200)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_desc1 = models.ImageField(upload_to=custom_image_path, default='/')
    image_desc2 = models.ImageField(upload_to=custom_image_path, default='/')
    image_desc3 = models.ImageField(upload_to=custom_image_path, default='/')
    image_desc4 = models.ImageField(upload_to=custom_image_path, default='/')
    image_desc5 = models.ImageField(upload_to=custom_image_path, default='/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Quản lí request"
