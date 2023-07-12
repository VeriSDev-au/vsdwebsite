from .models import BlogPost
from django.conf import settings

from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import QuerySet
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


from .category import CategoryCount

# Create your views here.


class BlogHomeView(ListView):
    model = BlogPost
    template_name = "blogs/blog_home.html"
    context_object_name = "posts"
    paginate_by = settings.MAX_DISPLAY_PAGINATION

    def get_queryset(self):
        posts = BlogPost.objects.all().order_by("-created_at")
        return posts
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["catInfos"] = CategoryCount.load_category_count()
        return context


class BlogSearchView(ListView):
    model = BlogPost
    template_name = "blogs/blog_search.html"
    context_object_name = "posts"
    paginate_by = settings.MAX_DISPLAY_PAGINATION

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

        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["catInfos"] = CategoryCount.load_category_count()
        context["searched"] = self.request.GET.get('searched')
        context["num_results"] = self.get_queryset().count()
        context["title"] = f"Search Result for \'{self.request.GET.get('searched')}\'"
        return context


class BlogCategoryView(ListView):
    model = BlogPost
    template_name = "blogs/blog_category.html"
    context_object_name = "posts"
    paginate_by = settings.MAX_DISPLAY_PAGINATION

    def get_queryset(self):
        category = self.request.GET.get('searched')
        posts = BlogPost.objects.all().filter(category__icontains=category).order_by("-created_at")
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category = self.request.GET.get('searched')

        context["catInfos"] = CategoryCount.load_category_count()
        context["num_results"] = self.get_queryset().count()
        context["title"] = f"List of all blogs item with category: {category}"
                            
        return context


class BlogPostDetailView(DetailView):
    template_name = "blogs/blog_detail.html"

    model = BlogPost