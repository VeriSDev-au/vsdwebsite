from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="vsd-home"),
    path("about/", views.about, name="vsd-about"),
    path("contact/", views.pages_contact, name="vsd-contact"),
]
