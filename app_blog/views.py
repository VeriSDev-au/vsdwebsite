from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from .models import BlogPost

# Create your views here.
class BlogHomeView(TemplateView):

    template_name = "blogs/blog_home.html"
    extra_context = {"posts": BlogPost.objects.all()}


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "blogs/blog_detail.html"
