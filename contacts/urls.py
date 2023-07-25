from django.urls import path, include
from . import views
from contacts import views

urlpatterns = [
    path('contacts/', views.all_Contacts())
]
