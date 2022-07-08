from django.urls import path
from blogapp import views
urlpatterns=[
    path("home",views.IndexView.as_view(),name="home"),
    path("accounts/signup",views.SignUpView.as_view(),name="signup"),
    path("accounts/signin",views.LoginView.as_view(),name="signin"),
    path("accounts/signout",views.sign_out,name="signout"),
    path("users/profile/add",views.CreateUserProfileView.as_view(),name="add-profile"),
    path("users/profile",views.ViewMyProfileView.as_view(),name="view-profile"),
    path("users/password/change",views.PasswordResetView.as_view(),name="password-reset"),
    path("users/profile/change/<int:user_id>",views.ProfileUpdateView.as_view(),name="profile-update"),
    path("users/profilepic/change/<int:user_id>",views.ProfilepicUpdateView.as_view(),name="profilepic-update"),
    path("posts/comment/<int:post_id>",views.add_comment,name="add-comment"),
    path("posts/like/add/<int:post_id>",views.add_like,name="add-like"),
]