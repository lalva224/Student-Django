
from django.contrib import admin
from django.urls import path,register_converter
from .views import All_Subjects
from student_app.converter import Int_Or_Str_Converter
register_converter(Int_Or_Str_Converter,'int_or_str')

urlpatterns= [
    path('<int_or_str:data>/',All_Subjects.as_view(),name = 'a_subject')
]