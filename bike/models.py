from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bike(models.Model):
    #bike_id = models.IntegerField(null=False, unique=True)
    reserved = models.IntegerField(default=0, null=False)
    current_owner = models.CharField(max_length=256, default="None", null=True)
    reservator = models.CharField(max_length=256, default="None", null=True)
    parking_name = models.CharField(max_length=256, default="NDK", null=False)

class BikeReservation(models.Model):
    bike_id = models.ForeignKey(Bike, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class BikeRent(models.Model):
    bike_id = models.ForeignKey(Bike, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    