from django.contrib import admin
from django.urls import path, include
from contacts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contacts.urls')),
    path('contacts/', views.all_Contacts())
]
