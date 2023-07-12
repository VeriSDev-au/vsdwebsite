from django.urls import path
from . import views as main_view

urlpatterns = [
    path("", main_view.HomeDashboard.as_view(), name="vsd-home"),
    path("contact/", main_view.pages_contact, name="vsd-contact"),
    path("blog2", main_view.pages_blog2, name="vsd-blog2")
]
