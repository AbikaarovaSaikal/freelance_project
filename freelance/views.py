from django.shortcuts import render
from .models import Job

# Create your views here.

def home(request):
    return render(request, "main_page.html")

def freelance_list(request):
    freelance = Job.objects.all()
    freelance_python = Job.objects.filter(name='python')
    return render(request, 'freelance/freelance_list.html', context={"freelance": freelance})

def freelance_detail(request, freelance_id):
    freelance = Job.objects.filter(id=freelance_id).first()
    return render(request, "freelance/freelance_detail.html", context={"freelance": freelance})
