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
        response['list'] = json.loads(serializers.serialize("json", account))

        response['msg'] = '成功显示所有帐号信息'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = '获取账号信息失败'
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
        response['msg'] = '用户名或者密码错误'
        response['error_num'] = 1
        return JsonResponse(response)
    response['msg'] = '成功登陆： '+r_username
    response['info']= Account.objects.get(username=r_username,password=r_password).user_type
    response['error_num'] = 0


    return JsonResponse(response)

@require_http_methods(["POST"])
def add_account(request):
    post_body=json.loads(request.body)
    r_username=post_body['username']
    r_password=post_body['password']
    print(r_username,r_password)
    r_user_type=1
    response = {}

    try:
        Account.objects.get(username=r_username,password=r_password)
    except Exception as e:  #0个或者多个
        if r_username == 'admin':
            r_user_type = 3
        elif r_username == 'gao':
            r_user_type = 2
            
        Account.objects.create(username=r_username,password=r_password,user_type=r_user_type)
        response['msg'] = '成功注册帐号： '+r_username
        response['error_num'] = 0
        return JsonResponse(response)
    
    response['msg'] = '该帐号已存在'
    response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["POST"])
def delete_account(request):     #与之相关的课程评价都需要删除
    post_body=json.loads(request.body)
    r_user_name=post_body['user_name']
    print(r_user_name)


    response = {}
    try:
        Account.objects.get(username=r_user_name)
    except  Exception as e:
        response['msg'] = '此账号不存在： '+r_user_name
        response['error_num'] = 1
        return JsonResponse(response)
    
    Account.objects.filter(username=r_user_name).delete()
    ChoiceComment.objects.filter(author_name=r_user_name).delete()
    TextComment.objects.filter(author_name=r_user_name).delete()

    response['msg'] = '成功删除帐号：' + r_user_name
    response['error_num'] = 0

    return JsonResponse(response)

@require_http_methods(["POST"])
def modify_account(request):     #与之相关的课程评价都需要删除
    post_body=json.loads(request.body)
    r_user_name = post_body['user_name']
    r_password=post_body['password']
    print(r_user_name,r_password)

    response = {}
    try:
        Account.objects.get(username=r_user_name)
    except  Exception as e:
        response['msg'] = '此账号不存在： '+r_user_name
        response['error_num'] = 1
        return JsonResponse(response)
    
    Account.objects.filter(username=r_user_name).update(password=r_password)

    response['msg'] = '成功修改帐号：' + r_user_name + '的密码'
    response['error_num'] = 0

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
        response['msg'] = '成功增加课程： '+r_course_name + ' '+r_teacher_name
        response['error_num'] = 0
        return JsonResponse(response)
    
    response['msg'] = '该课程已存在'
    response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_courses(request):
    response = {}
    try:
        courses = Course.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", courses))
        response['msg'] = '成功显示所有课程'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = '获取所有课程失败'
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["POST"])
def delete_course(request):     #与之相关的课程评价都需要删除
    post_body=json.loads(request.body)
    r_course_name=post_body['course_name']
    r_teacher_name=post_body['teacher_name']
    print(r_course_name,r_teacher_name)
    
    Course.objects.filter(course_name=r_course_name, teacher_name=r_teacher_name).delete()
    ChoiceComment.objects.filter(course_name=r_course_name,teacher_name=r_teacher_name).delete()
    TextComment.objects.filter(course_name=r_course_name,teacher_name=r_teacher_name).delete()
    
    response = {}
    try:
        response['msg'] = '成功删除课程：' + r_course_name +' '+r_teacher_name
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = '删除课程失败'
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["POST"])
def modify_course(request):     #与之相关的课程评价都需要删除
    post_body=json.loads(request.body)
    r_course_name=post_body['course_name']
    r_teacher_name = post_body['teacher_name']
    aim_course_name = post_body['aim_course_name']
    aim_teacher_name = post_body['aim_teacher_name']
    
    print(r_course_name,r_teacher_name,aim_course_name,aim_teacher_name)
    
    Course.objects.filter(course_name=r_course_name, teacher_name=r_teacher_name).update(course_name=aim_course_name,teacher_name=aim_teacher_name)
    ChoiceComment.objects.filter(course_name=r_course_name,teacher_name=r_teacher_name).update(course_name=aim_course_name,teacher_name=aim_teacher_name)
    TextComment.objects.filter(course_name=r_course_name,teacher_name=r_teacher_name).update(course_name=aim_course_name,teacher_name=aim_teacher_name)
    
    response = {}
    response['msg'] = '成功修改课程：' + r_course_name +' '+r_teacher_name
    response['error_num'] = 0

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
        response['msg'] = '成功评价该课程'
        response['error_num'] = 0
        return JsonResponse(response)
    
    response['msg'] = '您已经评价过此课程'
    response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_choicecomments(request):
    response = {}
    try:
        choicecomments = ChoiceComment.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", choicecomments))
        response['msg'] = '成功显示评价'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = '获取评价信息失败'
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
    count = result.count()
    if count == 0:
        response['msg'] = '当前课程暂时没有评价!'
        response['error_num'] = 1
        response['result']=[]
        return JsonResponse(response)
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
    response['msg'] = '成功显示评价!'
    response['error_num'] = 0
    response['result']=content_list
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_textcomments(request):
    response = {}
    try:
        textcomments = TextComment.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", textcomments))
        response['msg'] = '成功显示评价'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = '获取评价信息失败'
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

    print(r_course_name, r_teacher_name, r_author_name, r_content)
    response={}
    try:
        TextComment.objects.get(course_name=r_course_name,teacher_name=r_teacher_name,author_name=r_author_name)
    except Exception as e:
        TextComment.objects.create(course_name=r_course_name,teacher_name=r_teacher_name,author_name=r_author_name,content=r_content)
        response['msg'] = '成功评价该课程'
        response['error_num'] = 0
        return JsonResponse(response)
    
    response['msg'] = '您已经评价过此课程'
    response['error_num'] = 1
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


    file_name = open("diy.txt")
    jieba.load_userdict(file_name)
    
    for i in result:
        print(i.content)
        seg_list=jieba.cut(i.content,cut_all=True)
        liststr = "/".join(seg_list)

        for myword in liststr.split('/'):
            if not(myword.strip() in f_stop_seg_list):
                mywordlist.append(myword)
    mywordlist.sort()
    print(mywordlist)
    last = ""
    count = 0
    dict = {}
    
    for x in mywordlist:
        if last == "":
           last = x
           count += 1
        elif last != x:
            dict[last] = count
            last = x
            count = 1
        elif last == x:
            count += 1
    dict[last]=count
    print(dict)
    
    response['msg'] = '成功!'
    response['error_num'] = 0
    response['result']=dict
    return JsonResponse(response)

@require_http_methods(["POST"])
def delete_evaluation(request):     #与之相关的课程评价都需要删除 ChoiceComment  TextComment
    post_body = json.loads(request.body)
    r_user_name=post_body['user_name']
    r_course_name=post_body['course_name']
    r_teacher_name=post_body['teacher_name']
    print(r_user_name,r_course_name,r_teacher_name)
    
    a=ChoiceComment.objects.filter(author_name=r_user_name,course_name=r_course_name,teacher_name=r_teacher_name)
    b=TextComment.objects.filter(author_name=r_user_name,course_name=r_course_name,teacher_name=r_teacher_name)
    
    response = {}

    if len(a) + len(b) == 0:
        response['msg'] = '没有目标评价'
        response['error_num'] = 1
        return JsonResponse(response)
    else:
        a.delete()
        b.delete()
        response['msg'] = '成功删除评价：'
        response['error_num'] = 0
    return JsonResponse(response)

