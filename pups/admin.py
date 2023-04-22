from django.contrib import admin

# Register your models here.
from .models import  BabyDogs, Tag


admin.site.register(BabyDogs)
admin.site.register(Tag)