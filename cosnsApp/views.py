from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import cosnsModel
from django.contrib.auth.decorators import login_required

# Create your views here.


def signupfunc(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, "signup.html", {"some": 100})
        except IntegrityError:
            return render(request, "signup.html", {"error": "このユーザはすでに登録されています。"})
    return render(request, "signup.html")


def loginfunc(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, "login.html", {})
    return render(request, "login.html", {})


# @login_required
def listfunc(request):
    object_list = cosnsModel.objects.all()
    return render(request, "list.html", {"object_list": object_list})


def logoutfunc(request):
    logout(request)
    return redirect('login')


def detailfunc(request, pk):
    object = get_object_or_404(cosnsModel, pk=pk)
    return render(request, 'detail.html', {'object': object})


def goodfunc(request, pk):
    object = cosnsModel.objects.get(pk=pk)
    object.good = object.good + 1
    object.save()
    return redirect('list')


def readfunc(request, pk):
    object = cosnsModel.objects.get(pk=pk)
