from django.shortcuts import render, redirect
from .models import Job, Comment
from django.http import HttpResponse

from .form import FreelanceForm, SearchForm, CommentForm

from django.contrib.auth.decorators import login_required

from django.db.models import Q
# Create your views here.

def home(request):
    if request.method == "GET":
        return render(request, "main_page.html")

@login_required(login_url="/login/")
def freelance_list(request):
    freelance = Job.objects.all()
    if request.method == "GET":
        limit = 3
        forms = SearchForm()
        search = request.GET.get("search")
        category = request.GET.get("category")
        tags = request.GET.getlist("tags")
        ordering = request.GET.get("ordering")
        page = request.GET.get("page") if request.GET.get("page") else 1
        if category:
            freelance = freelance.filter(category=category)
        if search:
            freelance = freelance.filter(
                Q(name__icontains=search) | Q(description__icontains=search)
            )
        if tags:
            freelance = freelance.filter(tag__in=tags)
        
        if ordering:
            freelance = freelance.order_by(ordering)

        max_page = range(freelance.count() // limit+1)
        if page:
            freelance = freelance[limit * (int(page) - 1) : limit * int(page)]
        return render(
            request, 
            'freelance/freelance_list.html', 
            context={"freelance": freelance, "form": forms, "max_page": max_page[1:]},
            )

@login_required(login_url="/login/")
def freelance_detail(request, freelance_id):
    if request.method == "GET":
        freelance = Job.objects.filter(id=freelance_id).first()
        freelance.views += 1
        freelance.save()
        forms = CommentForm()
        comments = Comment.objects.filter(freelance_id=freelance_id)
        comments_count = comments.count()
        average = sum([comment.rate for comment in comments]) / comments_count if comments_count > 0 else 0
        return render(
            request, 
            "freelance/freelance_detail.html", 
            context={
                "freelance": freelance, 
                "form": forms, 
                "comments": comments,
                "average": average,
            },
        )
    elif request.method == "POST":
        if request.POST.get("action") == "comment":
            forms = CommentForm(request.POST)
            if forms.is_valid():
                Comment.objects.create(
                    text=forms.cleaned_data["text"],
                    freelance_id=freelance_id,
                    author=request.user,
                    rate=forms.cleaned_data["rate"]
                )
                return redirect(f"/freelance/{freelance_id}/")
        elif request.POST.get("action") == "delete":
            freelance = Job.objects.filter(id=freelance_id, user=request.user).filter()
            if freelance:
                freelance.delete()
            return redirect("/freelance/")
    
@login_required(login_url="/login/")
def freelance_create_view(request):
    if request.method == "GET":
        form = FreelanceForm()
        return render(request, "freelance/freelance_create.html", context={"form": form})
    elif request.method == "POST":
        form = FreelanceForm(request.POST, request.FILES)
        if form.is_valid():
            Job.objects.create(
                user=request.user,
                name=form.cleaned_data["name"],
                description=form.cleaned_data["description"],
                payment=form.cleaned_data["payment"],
                photo=form.cleaned_data["photo"],
            )
        return redirect("/profile/")

def freelance_update(request, freelance_id):
    if request.method == "GET":
        freelance = Job.objects.filter(id=freelance_id).first()
        form = FreelanceForm(initial=freelance.__dict__)
        return render(request, "freelance/freelance_update.html", context={"form": form})
    elif request.method == "POST":
        form = FreelanceForm(request.POST, request.FILES)
        if form.is_valid():
            freelance = Job.objects.filter(id=freelance_id).first()
            if request.user == freelance.user:
                freelance.name = form.cleaned_data["name"]
                freelance.description = form.cleaned_data["description"]
                freelance.price = form.cleaned_data["payment"]
                freelance.photo = form.cleaned_data["photo"]
                freelance.save()

        return redirect(f"/freelance/{freelance_id}/")