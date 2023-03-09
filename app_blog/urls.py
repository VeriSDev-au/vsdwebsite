from django.urls import path
from .views import BlogHomeView, BlogPostDetailView

urlpatterns = [
    path("blog/", BlogHomeView.as_view(), name="vsd-blog-home"),
    path("blog/<uuid:pk>/", BlogPostDetailView.as_view(), name="vsd-blog-detail"),
]
