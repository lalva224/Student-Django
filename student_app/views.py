from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import StudentAllSerializer,SubjectSerializer
from .models import Student,Subject
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
# Create your views here.

class All_Students(APIView):
    def get(self,request):
        #many=True because studentAll serializer could either be a queryobject or QuerySet of query Objects
        students = StudentAllSerializer(Student.objects.all(),many=True)
        #without data is merely of serializer class than of the class being
        return Response(students.data)

class All_Subjects(APIView):
    def get(self,request):
        subjects = SubjectSerializer(Subject.objects.all(),many=True)
        return Response(subjects.data)

class A_student(APIView):
    #will receive its id or name
    def get(self,request,id):
        try:
            stud = None
            if isinstance(id,int):
                stud = Student.objects.get(id=id)
            else:
                stud = Student.objects.get(name=id)
            
            student = StudentAllSerializer(Student.objects.get(id=id))
            return Response(student)  
        except Student.DoesNotExist:
            return NotFound('Student not found')

class A_subject(APIView):
    def get(self,request,data):
        try:
            subj = None
            if isinstance(data,int):
                subj = Subject.objects.get(id=data)
            else:
                subj = Subject.objects.get(subject_name=data)
            
            return Response(SubjectSerializer(subj).data)
        except Subject.DoesNotExist:
            return NotFound('Subject not found')

