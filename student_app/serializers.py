from rest_framework import serializers
from .models import Student
from subject_app.models import Subject
from grade_app.models import Grade
from subject_app.serializers import SubjectNameSerializer,SubjectSerializer

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["name", "student_email", "locker_number"]


class StudentAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name', 'student_email', 'personal_email', 'locker_number', 'locker_combination', 'good_student', 'subjects']
    
    def getSubjectId(self,obj):
        subjects = SubjectNameSerializer(obj.subjects.all(),many = True)
        subject_list = [subj.name for subj in subjects]
        return subject_list


