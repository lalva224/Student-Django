
from django.contrib import admin
from django.urls import path,register_converter
from .views import All_Subjects,CRUD_subject
from student_app.converter import Int_Or_Str_Converter
register_converter(Int_Or_Str_Converter,'int_or_str')

urlpatterns= [
    path('get/all/',All_Subjects.as_view(),name = 'all_subjects'),
    path('get/<int_or_str:data>/',CRUD_subject.as_view(),name = 'a_subject'),
    path('create/',CRUD_subject.as_view(),name = 'create_subject'),
    path('update/<int_or_str:info>/',CRUD_subject.as_view(),name = 'update_subject'),
    path('delete/<int_or_str:data>/',CRUD_subject.as_view(),name = 'delete_subject'),
]