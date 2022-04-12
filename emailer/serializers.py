from dataclasses import fields
from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ("id", "first_name", "last_name", "email", "company_name",
                  "comment", "is_broker", "is_owner", "is_charterer")
