from django.urls import path
from . import views

urlpatterns = [
    path('', views.em_index),
    path('data/', views.data),
    path('data/<int:id>', views.data_post),
]
