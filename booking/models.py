import uuid

from django.db import models

from authentication.models import User
from general.models import Vehicle


class BookingPost(models.Model):
    STATUS_CHOICES = (
        ('waiting', 'Chờ báo giá'),
        ('cancel', 'Hủy bỏ'),
        ('approved', 'Đã xác nhận'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    details = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="waiting")
    start_date = models.DateField()
    end_date = models.DateField()
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    price_min = models.DecimalField(max_digits=10, decimal_places=2)
    price_max = models.DecimalField(max_digits=10, decimal_places=2)
    num_of_people = models.PositiveIntegerField()
    allows_pet = models.BooleanField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # def add_bidder(self, user):
    #     if self.bidders.filter(id=user.id).exists():
    #         raise Exception("User has bid on this post")
    #
    #     if self.bidders.count() >= 5:
    #         raise Exception("The number of bidders has reached the maximum limit (5 people)")
    #
    #     self.bidders.add(user)
