from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import render

class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, null=True)
    u_school = models.CharField(max_length=255)
    u_project = models.CharField(max_length=255)
    u_major = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField()
#     majors = models.CharField(max_length=255) #원하는 전공
    
#     def __str__(self):
#         return self.user.username
    
# class Match(models.Model):
#     user = models.ForeignKey(UserProfile, related_name='matches', on_delete=models.CASCADE)
#     matched_users = models.ManyToManyField(UserProfile, related_name='matched_users')
#     matched_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f'{self.user}의 매칭'

class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
class Major(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    

    