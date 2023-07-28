from django.urls import path
from . import views as main_view

urlpatterns = [
    path("", main_view.HomeDashboard.as_view(), name="vsd-home"),
    path("contact/", main_view.pages_contact, name="vsd-contact"),
    path("cert-dp-203/", main_view.pages_ext_url_DP_203, name="vsd-cert-dp-203"),
    
]
