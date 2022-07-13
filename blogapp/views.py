from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,TemplateView,UpdateView
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from blogapp.forms import UserRegistrationForm,LoginForm,UserProfileForm,PasswordRestForm,BlogForm,CommentForm,ImageResetForm
from django.contrib import messages
from django.urls import reverse_lazy
from blogapp.models import UserProfile,Blogs,Comments

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

class IndexView(CreateView):
    model= Blogs
    form_class=BlogForm
    success_url=reverse_lazy("home")
    template_name = "home.html"

    def form_valid(self,form):
        form.instance.author=self.request.user
        self.object=form.save()
        messages.success(self.request,"post has been saved")
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        blogs=Blogs.objects.all().order_by("-posted_date")
        context["blogs"]=blogs
        comment_form=CommentForm()
        context["comment_form"]=comment_form
        return context


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
                user.set_password(password2)
                user.save()
                messages.success(request,"password changed")
                return redirect("signin")
            else:
                messages.error(request,"invalid credentials")
                return render(request,self.template_name,{"form":form})

class ProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "profile-update.html"
    success_url = reverse_lazy("home")
    pk_url_kwarg = "user_id"

    def form_valid(self, form):
        messages.success(self.request,"Your Profile has been updated successfully")
        self.object = form.save()
        return super().form_valid(form)

class ProfilepicUpdateView(UpdateView):
    model = UserProfile
    form_class = ImageResetForm
    template_name = "profilepic-update.html"
    success_url = reverse_lazy("home")
    pk_url_kwarg = "user_id"

    def form_valid(self, form):
        messages.success(self.request, "Your Profile has been updated successfully")
        self.object = form.save()
        return super().form_valid(form)



def add_comment(request,*args,**kwargs):
    if request.method=="POST":
        blog_id=kwargs.get("post_id")
        blog=Blogs.objects.get(id=blog_id)
        user=request.user
        comment=request.POST.get("comment")
        Comments.objects.create(blog=blog,user=user,comment=comment)
        messages.success(request,"comment has been posted")
        return redirect("home")

def add_like(request,*args,**kwargs):
    blog_id=kwargs.get("post_id")
    blog=Blogs.objects.get(id=blog_id)
    blog.liked_by.add(request.user)
    blog.save()
    return redirect("home")


def sign_out(request,*args,**kwargs):
    logout(request)
    return redirect("signin")




