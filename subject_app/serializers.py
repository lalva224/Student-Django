from rest_framework import serializers
from .models import Subject
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Subject
        fiels = '__all__'

class SubjectNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['subject_name']