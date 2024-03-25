from django.contrib import admin
from student_app.models import Student
from grade_app.models import Grade
from subject_app.models import Subject
# Register your models here.
admin.site.register([Student,Grade,Subject])
