import uuid

from django.db import models

from authentication.models import User
from booking.models import BookingPost
from general.models import Vehicle
from rental.models import Brand, Model


class Proposal(models.Model):
    STATUS_CHOICES = (
        ('waiting', 'Chờ xác nhận'),
        ('successful', 'Thành công'),
        ('failed', 'Thất bại'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_post = models.ForeignKey(BookingPost, on_delete=models.CASCADE, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)

    price = models.PositiveIntegerField()
    license_plate = models.CharField(blank=True, max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="waiting")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.full_name} - {self.points_change} points"
