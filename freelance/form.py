from django import forms

class FreelanceForm(forms.Form):
    name = forms.CharField(max_length=15, min_length=3)
    description = forms.CharField(max_length=15)
    payment = forms.IntegerField()
    photo = forms.ImageField()