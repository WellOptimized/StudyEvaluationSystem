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
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    user_type=models.IntegerField
    login_state=models.IntegerField

class Course(models.Model):
    course_name=models.CharField(max_length=32)
    teacher_name=models.CharField(max_length=32)

class Comment(models.Model):
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    content=models.CharField(max_length=120)
    author_name=models.CharField(max_length=32)
    author_type=models.IntegerField






