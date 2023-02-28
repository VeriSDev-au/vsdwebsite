from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "base.html")


def pages_contact(request):
    return render(request, "pages-contact.html")


def about(request):
    # return render(request, "blog/about.html", {"title": "About"})
    return HttpResponse("<h1>VSD About</h1>")
