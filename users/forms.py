from django import forms

class RegisterForm(forms.Form):
    age = forms.IntegerField()
    photo = forms.ImageField()
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=100)
    confirm_password = forms.CharField(max_length=100)

    def clean(self):
        if self.cleaned_data["password"] != self.cleaned_data["confirm_password"]:
            raise forms.ValidationError("Password don't match!")
        return self.cleaned_data
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)