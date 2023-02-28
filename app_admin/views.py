from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.http.response import HttpResponse
from django.views.generic import FormView

from django.contrib.auth.views import LoginView

from .models import UserProfile
from .forms import UserProfileForm


class RegisterView(FormView):
    form_class = UserProfileForm
    template_name = "pages-register.html"


class LoginView(LoginView):
    template_name = "pages-login.html"


def pages_userprofile_update(request, pk):
    userprofile = UserProfile.objects.get(id=pk)
    form = UserProfileForm(instance=userprofile)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=userprofile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)

    context = {"form": form, "pk": pk}
    return render(request, "user-profile.html", context)


def pages_userprofile_password_update(request, pk):
    userprofile = UserProfile.objects.get(id=pk)
    form = UserProfileForm(instance=userprofile)

    if request.method == "POST":
        print("[OK] POST ")
        form = UserProfileForm(request.POST, instance=userprofile)

        print("Form.is_valid() = " + str(form.is_valid()))
        # if form.is_valid():
        # form.save()
        return redirect(f"/user-profile/{pk}")

    context = {"form": form}
    return render(request, "user-profile.html", context)


def check_duplicate_email(request):
    print("Execute here")
    email = request.POST.get("email")
    if get_user_model().objects.filter(email=email).exists():
        return HttpResponse("This email already exists")
    else:
        return HttpResponse("")


def clear(request):
    return HttpResponse("")
