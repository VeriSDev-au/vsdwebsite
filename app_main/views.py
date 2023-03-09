from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from django.http import HttpResponse
from app_blog.models import BlogPost
import requests
import json


# Create your views here.
def home(request):
    return render(request, "base.html")


class HomeDashboard(TemplateView):

    gh_api_allrepo = "https://api.github.com/user/repos"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer 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",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    response = requests.get(gh_api_allrepo, headers=headers)
    allRepoResult = response.json()
    publicRepoResult = list(
        filter(lambda repoResult: repoResult["visibility"] == "public", allRepoResult)
    )
    totalGitHubPublicRespository = len(publicRepoResult)

    gh_api_activities = "https://api.github.com/users/VeriSDev-au/events"
    response = requests.get(gh_api_activities, headers=headers)
    allActivitiesResult = response.json()
    totalCommitInTheLast7Days = len(allActivitiesResult)

    # sortedAllActivitiesResult = allActivitiesResult.sort(
    #     key=lambda element: element.created_at, reverse=True
    # )

    sortedAllActivitiesResult = sorted(
        allActivitiesResult, key=lambda city: city["created_at"], reverse=True
    )
    top5SortedAllActivitiesResult = [x for x in sortedAllActivitiesResult[0:5]]
    print(len(top5SortedAllActivitiesResult))

    # now = datetime.datetime.now() + datetime.timedelta(seconds=60 * 3.4)
    # top5Final = []
    # for x in top5SortedAllActivitiesResult:
    #     top5Final.append(
    #         {"name": "Ha", "ago": timeago.format(datetime.date(x["created_at"]), now)}
    #     )

    template_name = "dashboard.html"
    extra_context = {
        "posts": BlogPost.objects.all(),
        "ghpubrep": totalGitHubPublicRespository,
        "ghTotalCommits": totalCommitInTheLast7Days,
        "ghTop5SortedAllActivitiesResult": top5SortedAllActivitiesResult,
    }


def pages_contact(request):
    return render(request, "pages-contact.html")


def about(request):
    # return render(request, "blog/about.html", {"title": "About"})
    return HttpResponse("<h1>VSD About</h1>")
