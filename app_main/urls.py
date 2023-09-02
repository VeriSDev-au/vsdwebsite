from django.urls import path
from . import views as main_view

urlpatterns = [
    path("", main_view.HomeDashboard.as_view(), name="vsd-home"),
    path("contact/", main_view.ContactView.as_view(), name="vsd-contact"),
    path("contact-success/", main_view.pages_contact_success, name="vsd-contact-success"),

    # Certificate URL Shortcut    
    path("cert-dp-300-azure-dba/", main_view.pages_ext_url_DP_300_Azure_DBA, name="vsd-cert-dp-300"),

    path("cert-pl-300-powerbi-data-analyst/", main_view.pages_ext_url_PL_300_PowerBI_Data_Analyst, name="vsd-cert-pl-300"),

    path("cert-dp-203-azure-data-eng/", main_view.pages_ext_url_DP_203_Azure_Data_Eng, name="vsd-cert-dp-203"),

    path("cert-pcap-python/", main_view.pages_ext_url_PCAP_Python, name="vsd-cert-pcap-python"),

    path("cert-pcep-python/", main_view.pages_ext_url_PCEP_Python, name="vsd-cert-pcep-python"),

    path("cert-az-900-azure-fundamental/", main_view.pages_ext_url_AZ_900_Azure_Fundamental, name="vsd-cert-az-900"),

    path("cert-dp-500-azure-enterprise-data-analyst/", main_view.pages_ext_url_DP_500_Azure_Enterprise_Data_Analyst, name="vsd-cert-dp-500")
    # End Certificate URL Shortcut    
]
