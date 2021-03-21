from django.shortcuts import render

# Create your views here.

from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json

from django.shortcuts import HttpResponse
 
from .models import Account
from .models import Course
# Create your views here.


@require_http_methods(["GET"])
def show_accounts(request):
    response = {}
    try:
        account = Account.objects.filter()
        # response['list'] = json.loads(serializers.serialize("json", account))
        response['list'] = json.loads(serializers.serialize("json", account))

        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["POST"])
def login_account(request):
    post_body=json.loads(request.body)
    r_username=post_body['username']
    r_password=post_body['password']
    print(r_username,r_password)
    
    response = {}
    query_res=Account.objects.filter(username=r_username,password=r_password)
    if query_res:
        response['msg'] = 'success'
        response['error_num'] = 0
    else:
        response['msg'] = 'No such account'
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["POST"])
def register_account(request):
    post_body=json.loads(request.body)
    r_username=post_body['username']
    r_email=post_body['email']
    r_password=post_body['password']
    print(r_username,r_email,r_password)

    Account.objects.create(username=r_username,password=r_password)
    
    response = {}
    try:    
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def modify_account(request):
    post_body=json.loads(request.body)
    r_username=post_body['username']
    r_password=post_body['password']
    print(r_username,r_password)
    
    response = {}
    query_res=Account.objects.filter(username=r_username,password=r_password)
    if query_res:
        response['msg'] = 'success'
        response['error_num'] = 0
    else:
        response['msg'] = 'No such account'
        response['error_num'] = 1

    return JsonResponse(response)



@require_http_methods(["POST"])
def update_account(request):
    post_body=json.loads(request.body)
    r_username=post_body['username']
    r_email=post_body['email']
    r_password=post_body['password']
    print(r_username,r_email,r_password)

    Account.objects.create(username=r_username,password=r_password)
    
    response = {}
    try:    
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["POST"])
def add_course(request):
    post_body=json.loads(request.body)
    r_course_name=post_body['course_name']
    r_teacher_name=post_body['teacher_name']
    print(r_course_name,r_teacher_name)
    
    response = {}
    
    try:
        Course.objects.get(course_name=r_course_name,teacher_name=r_teacher_name)
    except  Exception as e:
        Course.objects.create(course_name=r_course_name,teacher_name=r_teacher_name)
        response['msg'] = 'success'
        response['error_num'] = 0
        return JsonResponse(response)
    
    response['msg'] = '已经存在一个相同的课程!'
    response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_courses(request):
    response = {}
    try:
        courses = Course.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", courses))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["POST"])
def delete_course(request):
    post_body=json.loads(request.body)
    r_course_name=post_body['course_name']
    r_teacher_name=post_body['teacher_name']
    print(r_course_name,r_teacher_name)
    
    Course.objects.filter(course_name=r_course_name,teacher_name=r_teacher_name).delete()

    response = {}
    try:
        courses = Course.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", courses))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)




