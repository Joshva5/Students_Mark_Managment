"""
URL configuration for stdmanage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from stdmanageapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('login/',views.login_view,name='login_view'),
    path('student_register/',views.student_register, name='student_register'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('mark/form/',views.mark_form,name='mark_form'),
    path('admin_view/',views.admin_view,name='admin_view'),
    path('students_view/',views.students_view,name='students_view'),
    path('update_view/<int:id>/',views.update_view,name='update_view'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('sign_out',views.sign_out,name='sign_out'),
    

   
]