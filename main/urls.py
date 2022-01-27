from django.urls import path

from . import views

urlpatterns = [
    path('', views.satr, name='home'),
]
