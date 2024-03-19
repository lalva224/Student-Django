"""
URL configuration for school_proj project.

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
from django.urls import path,register_converter
from student_app.views import All_Students,All_Subjects,A_student,A_subject
from student_app.converter import Int_Or_Str_Converter


register_converter(Int_Or_Str_Converter,'int_or_str')

urlpatterns = [
    path('admin/', admin.site.urls),
    #name can be used in html templates
    path('api/v1/students/',All_Students.as_view(),name='all_student'),
    path('api/v1/subjects/',All_Subjects.as_view(),name='all_subjects'),
    path('api/v1/students/<int_or_str:data>/',A_student.as_view(), name = 'a_student'),
    path('api/v1/subjects/<int_or_str:data>/',A_subject.as_view(),name = 'a_subject')
]
