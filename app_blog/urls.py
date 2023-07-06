from django.urls import path
from .views import BlogHomeView, BlogPostDetailView, BlogSearchView

urlpatterns = [
    path("blog/", BlogHomeView.as_view(), name="vsd-blog-home"),
    path("blog/<uuid:pk>/", BlogPostDetailView.as_view(),name="vsd-blog-detail"), 
    path("search/", BlogSearchView.as_view(), name="vsd-blog-search")
]
