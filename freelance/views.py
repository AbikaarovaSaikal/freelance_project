from django.shortcuts import render
from .models import Job
from django.http import HttpResponse

from .form import FreelanceForm

# Create your views here.

def home(request):
    if request.method == "GET":
        return render(request, "main_page.html")

def freelance_list(request):
    if request.method == "GET":
        freelance = Job.objects.all()
        return render(request, 'freelance/freelance_list.html', context={"freelance": freelance})

def freelance_detail(request, freelance_id):
    if request.method == "GET":
        freelance = Job.objects.filter(id=freelance_id).first()
        return render(request, "freelance/freelance_detail.html", context={"freelance": freelance})
    
def freelance_create_view(request):
    if request.method == "GET":
        form = FreelanceForm()
        return render(request, "freelance/freelance_create.html", context={"form": form})
    elif request.method == "POST":
        form = FreelanceForm(request.POST, request.FILES)
        if form.is_valid():
            Job.objects.create(
                name=form.cleaned_data["name"],
                description=form.cleaned_data["description"],
                payment=form.cleaned_data["payment"],
                photo=form.cleaned_data["photo"],
            )
        return HttpResponse("Vacancy created")
