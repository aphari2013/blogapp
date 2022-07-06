from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,TemplateView
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from blogapp.forms import UserRegistrationForm,LoginForm,UserProfileForm,PasswordRestForm
from django.contrib import messages
from django.urls import reverse_lazy
from blogapp.models import UserProfile
# Create your views here.

# def index(request):
#     return render(request,"base.html")

class SignUpView(CreateView):
    form_class=UserRegistrationForm
    template_name="registration.html"
    model=User
    success_url = reverse_lazy("signin")

    # def get(self,request,*args,**kwargs):
    #     form=self.form_class()
    #     return render(request,self.template_name,{"form":form})
    #
    # def post(self,request,*args,**kwargs):
    #     form=self.form_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, "Registration successfull")
    #         return redirect("signup")
    #     else:
    #         messages.error(request, "Failed")
    #         return render(request,self.template_name,{"form":form})

class LoginView(FormView):
    model=User
    form_class=LoginForm
    template_name="login.html"

    # def get(self,request,*args,**kwargs):
    #     form=self.form_class()
    #     return render(request,self.template_name,{"form":form})
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                print("success")
                return redirect("home")
            else:
                messages.error(request,"invalid credentials")
                return render(request,self.template_name,{"form":form})

class IndexView(TemplateView):
    template_name = "home.html"


class CreateUserProfileView(CreateView):
    model = UserProfile
    template_name = "add-profile.html"
    form_class = UserProfileForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"profile has been created")
        self.object=form.save()
        return super().form_valid(form)

class ViewMyProfileView(TemplateView):
    template_name = "view-profile.html"

class PasswordResetView(FormView):
    template_name = "passwordreset.html"
    form_class = PasswordRestForm
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            oldpassword=form.cleaned_data.get("old_password")
            password1=form.cleaned_data.get("new_password")
            password2=form.cleaned_data.get("confirm_password")
            user=authenticate(request,username=request.user.username,password=oldpassword)
            if user:
                
            else:
                messages.error(request,"invalid credentials")
                return render(request,self.template_name,{"form":form})


def sign_out(request,*args,**kwargs):
    logout(request)
    return redirect("signin")





