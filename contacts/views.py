from django.shortcuts import render
from django.http import JsonResponse
from .models import Contact
from .serilalizers import ContactSerializer


# Create your views here.

def all_Contacts(request):
    contacts = Contact.objects.all()
    serializer = ContactSerializer(contacts, many=True)
    return JsonResponse(serializer.data)
