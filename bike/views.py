from django.shortcuts import render

from .forms import BikeForm
from .models import Bike
# Create your views here.


def bike_creat_form(request):
    bike_form=BikeForm(request.POST or None)
    if bike_form.is_valid():
        bike_form.save()

    context={
        'form':bike_form
    }

    return render(request,'bike_creat.html',context)


def bike_view_details(request):
    obj=Bike.objects.get(id=1)

    context={
        'object':obj
    }

    return render(request,'bike_details.html',context)

