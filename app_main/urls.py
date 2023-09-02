from django.urls import path
from . import views as main_view

urlpatterns = [
    path("", main_view.HomeDashboard.as_view(), name="vsd-home"),
    path("contact/", main_view.ContactView.as_view(), name="vsd-contact"),
    path("contact-success/", main_view.pages_contact_success, name="vsd-contact-success"),

    # Certificate URL Shortcut    
    path("dp-300/", main_view.pages_ext_url_DP_300_Azure_DBA, name="vsd-cert-dp-300"),

    path("pl-300/", main_view.pages_ext_url_PL_300_PowerBI_Data_Analyst, name="vsd-cert-pl-300"),

    path("dp-203/", main_view.pages_ext_url_DP_203_Azure_Data_Eng, name="vsd-cert-dp-203"),

    path("pcap/", main_view.pages_ext_url_PCAP_Python, name="vsd-cert-pcap-python"),

    path("pcep/", main_view.pages_ext_url_PCEP_Python, name="vsd-cert-pcep-python"),

    path("az-900/", main_view.pages_ext_url_AZ_900_Azure_Fundamental, name="vsd-cert-az-900"),

    path("dp-500/", main_view.pages_ext_url_DP_500_Azure_Enterprise_Data_Analyst, name="vsd-cert-dp-500")
    # End Certificate URL Shortcut    
]
