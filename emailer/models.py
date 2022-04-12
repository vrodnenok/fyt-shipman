from django.db import models
from django.forms import ModelForm

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    company_name = models.CharField(max_length=75)
    email = models.EmailField()
    is_broker = models.BooleanField(default=True)
    is_owner = models.BooleanField(default=True)
    is_charterer = models.BooleanField(default=True)
    comment = models.TextField()


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = [
            # , 'company', 'is_broker', 'is_owner', 'is_charterer', 'comment'
            'first_name', 'last_name', 'company_name', 'email'
        ]
