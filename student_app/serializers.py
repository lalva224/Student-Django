from rest_framework import serializers
from .models import Student,Subject,Grade


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["name", "student_email", "locker_number"]

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Subject
        exclude = []

class StudentAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name', 'student_email', 'personal_email', 'locker_number', 'locker_combination', 'good_student', 'subjects']
    subjects = SubjectSerializer(many = True)

