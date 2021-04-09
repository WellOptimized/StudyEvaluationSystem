from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    path('show_accounts',views.show_accounts),  
    path('login_account',views.login_account),
    path('add_account',views.add_account),

    path('delete_account',views.delete_account),
    path('modify_account',views.modify_account),

    path('add_course',views.add_course),
    path('show_courses',views.show_courses),
    path('delete_course', views.delete_course),
    path('modify_course',views.modify_course),
    

    path('add_choicecomment',views.add_choicecomment),
    path('show_choicecomments',views.show_choicecomments),
    path('get_choice_results',views.get_choice_results),
    
    path('add_textcomment',views.add_textcomment),
    path('show_textcomments',views.show_textcomments),
    path('get_text_results', views.get_text_results),
    
    path('delete_evaluation',views.delete_evaluation),
]


###path('admin/', admin.site.urls),