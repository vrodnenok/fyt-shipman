from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets

from .models import Contact
from .serializers import ContactSerializer


# Create your views here.

@login_required
def em_index(request):
    return render(request, template_name='em_index.html')


class ContactVewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by("id")
    serializer_class = ContactSerializer
