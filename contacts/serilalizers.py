from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'firstName', 'lastName', 'phoneNumber', 'emailAddress', 'birthday', 'facebookLink',
                  'twitterLink', 'instagramLink', 'notes')
