from django.db import models
from django.contrib.auth.models import AbstractUser


class ClassLevel(models.Model):
    level = models.CharField(max_length=100)
    total_student = models.IntegerField()

class Student(models.Model):
    first_name = models.CharField(max_length=255,null=False,blank=False)
    last_name = models.CharField(max_length=255,null=False,blank=False)
    email = models.CharField(max_length=255,null=False,blank=False)
    password = models.CharField(max_length=255)
    classLevel = models.ForeignKey(ClassLevel,on_delete=models.CASCADE)

class Project(models.Model):
    Title = models.CharField(max_length=255,null=255,blank=255)
    student = models.ManyToManyField(Student)

class Admin(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

    