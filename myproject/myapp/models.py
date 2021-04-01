from __future__ import unicode_literals
from django.db import models

# Create your models here.

from enum import Enum
class User_TYPE(Enum):
    STUDENT=1
    TEACHER=2
    ADMINISTRATOR=3

class LOGIN_STATE(Enum):
    NOT_LOGIN=1
    LOGIN=2


class Account(models.Model):
    username=models.CharField(max_length=32,primary_key=True)
    password=models.CharField(max_length=32)
    user_type=models.IntegerField(default=0)    
    login_state=models.IntegerField(default=0)

class Course(models.Model):
    course_name=models.CharField(max_length=32)
    teacher_name=models.CharField(max_length=32)
    class Meta:
        unique_together=("course_name","teacher_name")

class ChoiceComment(models.Model):
    course_name=models.CharField(max_length=32)
    teacher_name=models.CharField(max_length=32)
    author_name=models.CharField(max_length=32)
    content_1=models.IntegerField(default=0)
    content_2=models.IntegerField(default=0)
    content_3=models.IntegerField(default=0)
    content_4=models.IntegerField(default=0)
    content_5=models.IntegerField(default=0)

class TextComment(models.Model):
    course_name=models.CharField(max_length=32)
    teacher_name=models.CharField(max_length=32)
    author_name=models.CharField(max_length=32)
    content=models.CharField(max_length=256)






