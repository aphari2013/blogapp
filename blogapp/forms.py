from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from blogapp.models import UserProfile

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())

class UserProfileForm(ModelForm):
    class Meta:
        model=UserProfile
        exclude=("user",)
        widgets={
            "date_of_birth":forms.DateInput(attrs={"class":"form-control","type":"date"})
        }
class PasswordRestForm(forms.Form):
    old_password=forms.CharField(widget=forms.PasswordInput)
    new_password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField()
