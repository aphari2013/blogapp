from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    profile_pic=models.ImageField(upload_to="profile_pics",null=True)
    bio=models.CharField(max_length=120)
    phone=models.CharField(max_length=120)
    date_of_birth=models.DateField(null=True)
    options=(
        ("male","male"),
        ("female","female"),
        ("others","others")

    )
    gender=models.CharField(max_length=12,choices=options,default="male")
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="users")

class Blogs(models.Model):
    title=models.CharField(max_length=120)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to="blogimages",null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="author")
    posted_date=models.DateField(auto_now_add=True)
    liked_by=models.ManyToManyField(User)
    def __str__(self):
        return self.title


class Comments(models.Model):
    blog=models.ForeignKey(Blogs,on_delete=models.CASCADE)
    comment=models.CharField(max_length=160)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

#users=[1.anj,2.django,3.python]