from json import JSONDecoder
import json
from django.shortcuts import render
from django.http import QueryDict, JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.forms.models import modelform_factory

from .models import Contact, ContactForm


# Create your views here.

@login_required
def em_index(request):
    return render(request, template_name='em_index.html')


@login_required
def data_post(request, id):
    request_unicode = request.body.decode('utf-8')
    print(request_unicode)
    if request.method == 'POST':
        modelform = modelform_factory(Contact, ContactForm)
        form = modelform(request.POST)
        print(form.is_valid())
        if form.is_valid():
            obj = form.save()
            return JsonResponse({'id': obj.pk})
        else:
            return JsonResponse({'status': "error"})
    elif request.method == 'PUT':
        modelform = modelform_factory(Contact, ContactForm)
        contact = Contact.objects.get(pk=id)
        form = modelform(QueryDict(request_unicode), instance=contact)
        if form.is_valid():
            print('form is valid')
            form.save()
            return JsonResponse({})
        else:
            return JsonResponse({'status': 'error', 'message': "error"}, status=500)

    #delete
    elif request.method == 'DELETE':
        Contact.objects.get(pk=id).delete()
        return JsonResponse({})


@login_required
def data(request):
    #get all data
    print(request.user)
    if request.method == 'GET':
        contacts = Contact.objects.all()
        data = [{'id': item.pk,
                 'first_name': item.first_name,
                 'last_name': item.last_name,
                 'company_name': item.company_name,
                 'email': item.email, 'is_owner': item.is_owner,
                 'is_broker': item.is_broker, 'is_charterer': item.is_charterer,
                 'comment': item.comment
                 } for item in contacts]
        return JsonResponse(data, safe=False)

    #update
    request_unicode = request.body.decode('utf-8')
    print(request.body)
    if request.method == 'POST':
        modelform = modelform_factory(Contact, ContactForm)
        form = modelform(request.POST)
        print(form.is_valid())
        if form.is_valid():
            obj = form.save()
            return JsonResponse({'id': obj.pk})
        else:
            return JsonResponse({'status': "error"})
    elif request.method == 'PUT':
        modelform = modelform_factory(Contact, ContactForm)
        contact = Contact.objects.get(pk=id)
        print(f"And contact Id is = {contact.id}")
        form = modelform(QueryDict(request.body), instance=contact)
        if form.is_valid():
            form.save()
            return JsonResponse({})
        else:
            return JsonResponse(form)

    #delete
    elif request.method == 'DELETE':
        Contact.objects.get(pk=id).delete()
        return JsonResponse({})
