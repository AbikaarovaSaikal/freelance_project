from django.shortcuts import render
from django.contrib.auth.models import User
from users.forms import LoginForm, RegisterForm
from django.http import HttpResponse
# Create your views here.

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout

def register_view(request):
    if request.method == "GET":
        forms = RegisterForm()
        return render(request, "users/register.html", context={"form": forms})
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.cleaned_data.__delitem__("confirm_password")
            User.objects.create_user(**form.cleaned_data)
            return HttpResponse("User created")
        return HttpResponse("Invalid form")
    
def login_view(request):
    if request.method == "GET":
        forms_obj = LoginForm()
        return render(request, "users/login.html", context={"form": forms_obj})
    elif request.method == "POST":
        forms_obj = LoginForm(request.POST)
        if forms_obj.is_valid():
            user = authenticate(**forms_obj.cleaned_data)
            login(request, user)
            return HttpResponse("User logged in")
        
@login_required(login_url="/login/")
def logout_view(request):
    if request.method == "GET":
        logout(request)
        return HttpResponse("User logged out")