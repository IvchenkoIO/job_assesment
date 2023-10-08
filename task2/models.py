from django.db import models

# Create your models here.
from django.db import models

class Reservations(models.Model):
    quest_name = models.CharField(max_length=255)
    status=models.CharField(max_length=255)
    flat_booked=models.CharField(max_length=255)
    checkin_date=models.DateField()
    checkout_date=models.DateField()
    guest_email=models.CharField(max_length=255)
    phone_number=models.CharField(max_length=255)
    booking_value=models.FloatField()

    class Meta:
        app_label = 'task2'