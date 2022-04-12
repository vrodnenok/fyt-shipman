from django.urls import include, path, re_path
from . import views
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'data/?', views.ContactVewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path('', views.em_index),
]
