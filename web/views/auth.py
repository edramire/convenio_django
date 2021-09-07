from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def login(request):
    if request.method == "GET":
        return render(
            request, "auth/login.html"
        )
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print('user')
        print(user)
        if user is not None:
            auth_login(request, user)
            return redirect(reverse("projects"))
        else:
            return redirect(reverse("login"))

def logout(request):
    auth_logout(request)
    return redirect(reverse("login"))
