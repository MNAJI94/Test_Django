from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexn, name= "index"),
]