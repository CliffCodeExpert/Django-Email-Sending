from .import views
from django.urls import path

urlpatterns = [
    path("",views.sending_gmail,name='sending_gmail'),
]
