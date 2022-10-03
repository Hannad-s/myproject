from importlib.resources import path
from django.urls import path, include
from pages import views



urlpatterns = [
    path('',views.index),
]





