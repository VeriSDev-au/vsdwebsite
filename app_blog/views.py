from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from .models import BlogPost
from django.db.models import QuerySet

# Create your views here.


class BlogHomeView(TemplateView):
    template_name = "blogs/blog_home.html"

    def get_context_data(self, **kwargs):
        posts = BlogPost.objects.all()
        posts = QuerySet(model=BlogPost, query=posts.query)
        
        extra_context = {"posts": BlogPost.objects.all()}
        return extra_context


class BlogSearchView(TemplateView):
    template_name = "blogs/blog_search.html"

    def get_context_data(self, **kwargs):
        posts = BlogPost.objects.all()
        posts = QuerySet(model=BlogPost, query=posts.query)
        
        extra_context = {"posts": BlogPost.objects.all()}
        return extra_context


class BlogPostDetailView(DetailView):
    template_name = "blogs/blog_detail.html"

    model = BlogPost
    
