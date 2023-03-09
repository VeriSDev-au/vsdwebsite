from django.urls import path
from . import views as main_view

urlpatterns = [
    path("", main_view.HomeDashboard.as_view(), name="vsd-home"),
    path("about/", main_view.about, name="vsd-about"),
    path("contact/", main_view.pages_contact, name="vsd-contact"),
]
