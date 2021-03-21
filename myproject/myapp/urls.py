from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    path('show_accounts',views.show_accounts),  
    path('login_account',views.login_account),
    path('register_account',views.register_account),

    # path('delete_account',views.delete_account),
    # path('modify_account',views.views.modify_account),

    path('add_course',views.add_course),
    path('show_courses',views.show_courses),
    path('delete_course',views.delete_course),
]


###path('admin/', admin.site.urls),