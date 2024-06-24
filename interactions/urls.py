from django.urls import path
from . import views

urlpatterns = [
    path("", views.interactions, name="interactions"),
]
