import os
import requests

from django.shortcuts import render
from django.views.generic import TemplateView

from app_blog.models import BlogPost


# # Create your views here.
# def home(request):
#     """Render home page to the client"""
#     return render(request, "base.html")


class HomeDashboard(TemplateView):
    """Render dashboard as home page to the client"""

    template_name = "dashboard.html"

    def get_context_data(self, *args, **kwargs):
        print('HomeDashboard.get_context_data')
        extra_context = super().get_context_data(*args, **kwargs)

        # Get the total GitHub Public Repository
        gh_api_allrepo = "https://api.github.com/user/repos"
        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer " + str(os.environ.get("VSD_GITHUB_TOKEN")),
            "X-GitHub-Api-Version": "2022-11-28",
        }
        gh_api_all_repo_response = requests.get(gh_api_allrepo,
                                                headers=headers,
                                                timeout=10)

        gh_api_all_repo_result = gh_api_all_repo_response.json()
        total_github_public_repo = len(
            list(
                filter(
                    lambda repo_result: repo_result["visibility"] == "public",
                    gh_api_all_repo_result,
                )
            )
        )
        # End Get the total GitHub Public Repository

        # Get the total GitHub commit
        gh_api_activities = "https://api.github.com/users/VeriSDev-au/events"
        gh_api_activities_response = requests.get(
            gh_api_activities,
            headers=headers,
            timeout=10
        )
        gh_api_activities_result = gh_api_activities_response.json()
        total_github_commit_in_the_last_7days = len(gh_api_activities_result)
        # End Get the total GitHub commit

        gh_api_activities_sorted = sorted(
            gh_api_activities_result,
            key=lambda city: city["created_at"],
            reverse=True
        )
        gh_topx_activities_result = [x for x in gh_api_activities_sorted[0::]]

        # Query 5 latest posted blog
        blog_post_5_last_posts = BlogPost.objects.all().order_by("created_at")[:5:-1]
        sequence = 1
        for blog_post_5_last_post_item in blog_post_5_last_posts:
            blog_post_5_last_post_item.seq = sequence
            sequence += 1
        
        extra_context = {
            "posts": blog_post_5_last_posts,
            "ghpubrep": total_github_public_repo,
            "ghTotalCommits": total_github_commit_in_the_last_7days,
            "gh_topx_activities_result": gh_topx_activities_result,
        }
        return extra_context



def pages_contact(request):
    """Render the contact page to the client"""
    return render(request, "contact.html")
