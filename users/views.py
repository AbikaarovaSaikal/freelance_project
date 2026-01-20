from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from users.forms import LoginForm, RegisterForm
from django.http import HttpResponse
# Create your views here.

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from users.models import Profile

def register_view(request):
    if request.method == "GET":
        forms = RegisterForm()
        return render(request, "users/register.html", context={"form": forms})
    elif request.method == "POST":
        forms_obj = RegisterForm(request.POST)
        if forms_obj.is_valid():
            forms_obj.cleaned_data.__delitem__("confirm_password")
            age = forms_obj.cleaned_data.pop("age")
            photo = forms_obj.cleaned_data.pop("photo")
            user = User.objects.create_user(**forms_obj.cleaned_data)
            if user:
                Profile.objects.create(user=user, age=age, photo=photo)
            return redirect("/login/")
        return HttpResponse("Invalid form")
    
def login_view(request):
    if request.method == "GET":
        forms_obj = LoginForm()
        return render(request, "users/login.html", context={"form": forms_obj})
    elif request.method == "POST":
        forms_obj = LoginForm(request.POST)
        if forms_obj.is_valid():
            user = authenticate(**forms_obj.cleaned_data)
            if user:
                login(request, user)
            return redirect("/")
        
@login_required(login_url="/login/")
def logout_view(request):
    if request.method == "GET":
        logout(request)
        return redirect("/")
    
@login_required(login_url="/login/")
def profile_view(request):
    if request.method == "GET":
        user = request.user
        freelance = user.freelance.all()
        return render(request, "users/profile.html", context={"user": user, "freelance": freelance})