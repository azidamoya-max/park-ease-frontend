from django.db import models

# Create your models here.

class Guest(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    email_address = models.EmailField(unique=True, blank=False)
    date_registered = models.DateField(blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"