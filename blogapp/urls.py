from django.urls import path
from blogapp import views
urlpatterns=[
    path("home",views.IndexView.as_view(),name="home"),
    path("accounts/signup",views.SignUpView.as_view(),name="signup"),
    path("accounts/signin",views.LoginView.as_view(),name="signin"),
    path("accounts/signout",views.sign_out,name="signout"),
    path("users/profile/add",views.CreateUserProfileView.as_view(),name="add-profile"),
    path("users/profile",views.ViewMyProfileView.as_view(),name="view-profile"),
    path("users/password/change",views.PasswordResetView.as_view(),name="password-reset")
]