from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_blog, name='blog'),  # mainpage of my project
]
