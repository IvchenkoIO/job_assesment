from django.db import models
from django.contrib.auth.models import User, Group

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

class Reservations_1(models.Model):
    quest_name = models.CharField(max_length=255)
    status=models.CharField(max_length=255)
    flat_booked=models.CharField(max_length=255)
    checkin_date=models.DateField()
    checkout_date=models.DateField()
    creation_log=models.DateField()
    booking_value=models.FloatField()

    class Meta:
        app_label = 'task1'