from django import forms
from freelance.models import Category, Tag

class FreelanceForm(forms.Form):
    name = forms.CharField(max_length=15, min_length=3)
    description = forms.CharField(max_length=15)
    payment = forms.IntegerField()
    photo = forms.ImageField()

class SearchForm(forms.Form):
    ordering = [
        ("created_at", "Created At"),
        ("updated_at", "Updated At"),
        ("name", "Name"),
        ("payment", "Payment"),
        ("-created_at", "Created At(descinding)"),
        ("-updated_at", "Updated At(descinding)"),
    ]
    search = forms.CharField(max_length=100, required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), required=False
    )