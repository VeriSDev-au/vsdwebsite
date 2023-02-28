from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views as user_views

urlpatterns = [
    # User Profile
    path("register/", user_views.RegisterView.as_view(), name="vsd-admin-register"),
    path(
        "user-profile/<str:pk>",
        user_views.pages_userprofile_update,
        name="vsd-admin-profile",
    ),
    path(
        "user-password/<str:pk>",
        user_views.pages_userprofile_password_update,
        name="vsd-admin-profile-change-password",
    ),
    # EndUser Profile
    path("login/", user_views.LoginView.as_view(), name="vsd-admin-login"),
    path("logout/", LogoutView.as_view(), name="vsd-admin-logout"),
    path("clear/", user_views.clear, name="vsd-admin-clear"),
]

hmtx_views = [
    # User Registration
    path(
        "check-duplicate-email/",
        user_views.check_duplicate_email,
        name="check-duplicate-email",
    ),
    # User Registration
]

urlpatterns += hmtx_views
