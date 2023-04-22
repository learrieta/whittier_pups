from django.shortcuts import render
from django.urls import path 
from django.http import HttpResponse
from .models import BabyDogs

# Create your views here.


def  about_us(request):
    baby_dogs = BabyDogs.objects.all()
    context = {'baby': baby_dogs}
    return render(request,'pups/about-us.html', context)


def single_puppy(request, pk):
    litter = BabyDogs.objects.get(id = pk)
    context = {'single_puppy' : litter}
    return render(request,'pups/single_puppy.html', context)
