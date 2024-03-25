from django.shortcuts import render
from .serializers import SubjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .models import Subject
from rest_framework.exceptions import NotFound
# Create your views here.
class All_Subjects(APIView):
    def get(self,request):
        subjects = SubjectSerializer(Subject.objects.all(),many=True)
        return Response(subjects.data)

class CRUD_subject(APIView):
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
        
    def post(self,request):
        subject = SubjectSerializer(data=request.data)
        if subject.is_valid():
            subject.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status =status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,data):
        try:
            subject = None
            if isinstance(data,int):
                subject = Subject.objects.get(id=data)
            else:
                subject = Subject.objects.get(subject_name=data)
        except Subject.DoesNotExist:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        
        #a put just pass the request data, with a patch (partial update) you need the actual object
        updatedSubject = SubjectSerializer(subject,data=request.data)
        updatedSubject.save()
        return Response(status = status.HTTP_200_OK)
    
    def delete(self,request,data):
        try:
            subject = None
            if isinstance(data,int):
                subject = Subject.objects.get(id=data)
            else:
                subject = Subject.objects.get(subject_name=data)
        except Subject.DoesNotExist:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)