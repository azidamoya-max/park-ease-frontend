from django.db import models

# Create your models here.

class Room(models.Model):

    CATEGORY_CHOICES = [
        ('standard', 'Standard'),
        ('deluxe', 'Deluxe'),
        ('suite', 'Suite'),
        ('executive', 'Executive Suite'),
        ('presidential', 'Presidential Suite'),
    ]

    STATUS_CHOICES = [ 
        ('not_occupied', 'Not Occupied'),
        ('occupied', 'Occupied'),
    ]

    room_number = models.CharField(max_length=10, unique=True, blank=False)
    room_category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=False)
    room_status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='not_occupied', blank=False)

    def __str__(self):
        return f"Room {self.room_number} - {self.get_room_category_display()} - {self.get_room_status_display()}"