from django.shortcuts import render

# Create your views here.

from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json

from django.shortcuts import HttpResponse
 
from .models import Account
from .models import Course
from .models import ChoiceComment
from .models import TextComment

import jieba
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
    try:
        Account.objects.get(username=r_username,password=r_password)
    except Exception as e:   #0个或者多个
        response['msg'] = 'No such account'
        response['error_num'] = 1
        return JsonResponse(response)
    response['msg'] = 'success'
    response['error_num'] = 0


    return JsonResponse(response)

@require_http_methods(["POST"])
def add_account(request):
    post_body=json.loads(request.body)
    r_username=post_body['username']
    r_email=post_body['email']
    r_password=post_body['password']
    print(r_username,r_email,r_password)

    response = {}    
    try:
        Account.objects.get(username=r_username,password=r_password)
    except Exception as e:  #0个或者多个
        Account.objects.create(username=r_username,password=r_password)
        response['msg'] = 'success'
        response['error_num'] = 0
        return JsonResponse(response)
    
    response['msg'] = '已经存在一个相同的帐号!'
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
def delete_course(request):     #与之相关的课程评价都需要删除
    post_body=json.loads(request.body)
    r_course_name=post_body['course_name']
    r_teacher_name=post_body['teacher_name']
    print(r_course_name,r_teacher_name)
    
    Course.objects.filter(course_name=r_course_name,teacher_name=r_teacher_name).delete()
    

    response = {}
    try:
        courses = Course.objects.filter()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["POST"])
def add_choicecomment(request):
    post_body=json.loads(request.body)
    print(post_body)
    r_course_name=post_body['course_name']
    r_teacher_name=post_body['teacher_name']
    r_author_name=post_body['author_name']
    r_content_1=post_body['content_1']
    r_content_2=post_body['content_2']
    r_content_3=post_body['content_3']
    r_content_4=post_body['content_4']
    r_content_5=post_body['content_5']

    print(r_course_name,r_teacher_name,r_author_name,r_content_1,r_content_2,r_content_3,r_content_4,r_content_5)

    response = {}    
    try:
        ChoiceComment.objects.get(course_name=r_course_name,teacher_name=r_teacher_name,author_name=r_author_name)
    except Exception as e:
        ChoiceComment.objects.create(course_name=r_course_name,teacher_name=r_teacher_name,author_name=r_author_name,\
            content_1=r_content_1,content_2=r_content_2,content_3=r_content_3,content_4=r_content_4,content_5=r_content_5)
        response['msg'] = 'success'
        response['error_num'] = 0
        return JsonResponse(response)
    
    response['msg'] = '你已经评价过这个选择评价了!'
    response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_choicecomments(request):
    response = {}
    try:
        choicecomments = ChoiceComment.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", choicecomments))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def get_choice_results(request):
    post_body=json.loads(request.body)
    print(post_body)
    r_course_name=post_body['course_name']
    r_teacher_name=post_body['teacher_name']

    print(r_course_name,r_teacher_name)

    response = {}    
    
    result=ChoiceComment.objects.filter(course_name=r_course_name,teacher_name=r_teacher_name)
    count=result.count()
    content_list=[0,0,0,0,0]
    for row in result:
        content_list[0]+=row.content_1
        content_list[1]+=row.content_2
        content_list[2]+=row.content_3
        content_list[3]+=row.content_4
        content_list[4]+=row.content_5

    content_list=[x/count for x in content_list]
    for x in content_list:
        print(x)
    response['msg'] = '成功!'
    response['error_num'] = 0
    response['result']=content_list
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_textcomments(request):
    response = {}
    try:
        textcomments = TextComment.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", textcomments))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["POST"])
def add_textcomment(request):
    post_body=json.loads(request.body)
    print(post_body)
    r_course_name=post_body['course_name']
    r_teacher_name=post_body['teacher_name']
    r_author_name=post_body['author_name']
    r_content=post_body['content']

    print(r_course_name,r_teacher_name,r_author_name,r_content)

    TextComment.objects.create(course_name=r_course_name,teacher_name=r_teacher_name,author_name=r_author_name,content=r_content)
    response = {}    
    response['msg'] = 'success'
    response['error_num'] = 0
    return JsonResponse(response)

@require_http_methods(["POST"])
def get_text_results(request):
    post_body=json.loads(request.body)
    print(post_body)
    r_course_name=post_body['course_name']
    r_teacher_name=post_body['teacher_name']

    print(r_course_name,r_teacher_name)

    response = {}    
    
    result=TextComment.objects.filter(course_name=r_course_name,teacher_name=r_teacher_name)
    
    mywordlist = []

    f_stop = open("stopwords.txt")
    try:
        f_stop_text = f_stop.read()
    finally:
        f_stop.close()
    f_stop_seg_list = f_stop_text.split('\n')
    
    for i in result:
        print(i.content)
        seg_list=jieba.cut(i.content,cut_all=True)
        liststr = "/".join(seg_list)

        for myword in liststr.split('/'):
            if not(myword.strip() in f_stop_seg_list):
                mywordlist.append(myword)
    print(mywordlist)
    
    response['msg'] = '成功!'
    response['error_num'] = 0
    response['result']=mywordlist
    return JsonResponse(response)

