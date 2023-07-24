from django.db import models


# Create your models here.
from django.db.models import CharField


class Contact(models.Model):
    firstName: CharField = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=10)
    emailAddress = models.TextField(max_length=254)
    birthday = models.DateField()
    facebookLink = models.URLField(max_length=200)
    twitterLink = models.URLField(max_length=200)
    instagramLink = models.URLField(max_length=200)
    notes = models.TextField(max_length=300)

    def __str__(self):
        return self.firstName + ' ' + self.lastName

