
from django.contrib import admin
from django.urls import path,register_converter
from student_app.views import All_Students,CRUD_Student
from student_app.converter import Int_Or_Str_Converter
register_converter(Int_Or_Str_Converter,'int_or_str')

urlpatterns = [
    path('',All_Students.as_view(),name='all_student'),
    path('<int_or_str:data>/',CRUD_Student.as_view(), name = 'a_student'),
    path('update/<int_or_str:data>',CRUD_Student.as_view(),name = 'update_student'),
    path('create',CRUD_Student.as_view(),name = 'create_student'),
    path('delete/<int_or_str:data>',CRUD_Student.as_view(),name = 'delete_student')

]
