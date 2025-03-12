from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_admin_restaurant = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username


class Restaurant(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(blank=True, null=True)
    cuisine_type = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    admin = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="restaurants"
    )

    def __str__(self):
        return self.name


class Table(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="tables"
    )
    table_number = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number} in {self.restaurant.name} (Capacity: {self.capacity})"


class Reservation(models.Model):
    guest = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reservations"
    )
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name="reservations"
    )
    date = models.DateField()
    time = models.TimeField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"Reservation for {self.guest.username} at {self.table.restaurant.name} - {self.date} {self.time}"
