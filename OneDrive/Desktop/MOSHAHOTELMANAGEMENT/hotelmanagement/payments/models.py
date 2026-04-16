from django.db import models

from guests.models import Guest
from rooms.models import Room

# Create your models here.

from django.db import models
from guests.models import Guest
from rooms.models import Room


class Payment(models.Model):
    PAYMENT_TYPE_CHOICES = [
        ('mobile_money', 'Mobile Money'),
        ('cash', 'Cash'),
    ]

    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES, blank=False)
    payment_date = models.DateField(blank=False)

    def __str__(self):
        return f"{self.guest} - Room {self.room.room_number} - UGX {self.amount:,.0f}"