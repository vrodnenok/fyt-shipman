from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'), #mainpage of my project
]
