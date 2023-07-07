from .models import BlogPost

from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from django.db.models import QuerySet
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from .category import CategoryCount

# Create your views here.


class BlogHomeView(TemplateView):
    model = BlogPost
    template_name = "blogs/blog_home.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = BlogPost.objects.all()
        
        context["catInfos"] = CategoryCount.load_category_count()
        context["posts"] = posts
        return context


class BlogSearchView(TemplateView):
    model = BlogPost
    template_name = "blogs/blog_search.html"
    context_object_name = "posts"

    def get_queryset(self):
        searched = self.request.GET.get("searched")
        posts = BlogPost.objects.all()

        search_vector = SearchVector("title", weight="A") + SearchVector("intro", weight="B") + SearchVector("body", weight="D")

        search_query = SearchQuery(searched)
        
        return (
            posts.annotate(search=search_vector,
                           rank=SearchRank(search_vector,                            search_query)
            )
            .filter(search=search_query)
            .order_by("-rank")
        )
        

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        posts = self.get_queryset()
               
        context["catInfos"] = CategoryCount.load_category_count()
        context["searched"] = self.request.GET.get('searched')
        context["num_results"] = posts.count()
        context["posts"] = posts
        context["title"] = f"Search Result for \'{self.request.GET.get('searched')}\'"
        return context


class BlogPostDetailView(DetailView):
    template_name = "blogs/blog_detail.html"

    model = BlogPost
    
