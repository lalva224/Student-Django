from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import StudentAllSerializer,SubjectSerializer
from .models import Student
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status

# Create your views here.

class All_Students(APIView):
    def get(self,request):
        #many=True because studentAll serializer could either be a queryobject or QuerySet of query Objects
        students = StudentAllSerializer(Student.objects.all(),many=True)
        #without data is merely of serializer class than of the class being
        return Response(students.data)


class CRUD_Student(APIView):
    #will receive its id or name
    def get(self,request,data):
        try:
            stud = None
            if isinstance(data,int):
                stud = Student.objects.get(id=data)
            else:
                stud = Student.objects.get(name=data.title())
            
            return Response(StudentAllSerializer(stud).data,status=status.HTTP_200_OK)  
        except Student.DoesNotExist:
            return NotFound('Student not found')
    
    def post(self,request):
        student = StudentAllSerializer(data=request.data)
        if student.is_valid():
            student.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(student.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,data):
        student = None
        if isinstance(data,int):
            student = Student.objects.get(id=data)
        else:
            student = Student.objects.get(name = data.title())
        
        studentSerializer = StudentAllSerializer(student,data=request.data)
        if studentSerializer.is_valid():
            studentSerializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(studentSerializer.errors)
    
    def delete(self,request,data):
        student = None
        try:
            if isinstance(data,int):
                student = Student.objects.get(id=data)
            else:
                student = Student.objects.get(name=data.title())
        except student.DoesNotExist:
             return Response(status=status.HTTP_404_NOT_FOUND)
        
        #serializer does not have delete
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




        

        




    
        


