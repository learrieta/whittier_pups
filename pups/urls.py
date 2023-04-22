from django.urls import path
from . import views

urlpatterns = [

    path('', views.about_us, name='about_us'),
    path('single_puppy/<str:pk>/', views.single_puppy, name='single_puppy'),

]