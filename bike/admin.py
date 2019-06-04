from django.contrib import admin
from . models import Bike,BikeReservation,BikeRent
# Register your models here.

admin.site.register(Bike)
admin.site.register(BikeReservation)
admin.site.register(BikeRent)