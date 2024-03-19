from django.db import models
from django.core import validators as v
from .validators import (
    validate_combination_format,
    validate_name_format,
    validate_school_email,
    validate_professor_name,
    validate_subject_format
)


# Create your models here.
class Student(models.Model):

    name = models.CharField(
        max_length=255, null=False, blank=False, validators=[validate_name_format]
    )
    student_email = models.EmailField(
        null=False, blank=False, unique=True, validators=[validate_school_email]
    )
    personal_email = models.EmailField(null=False, blank=False, unique=True)
    locker_number = models.IntegerField(
        default=110,
        null=False,
        blank=False,
        unique=True,
        validators=[v.MinValueValidator(1), v.MaxValueValidator(200)],
    )
    locker_combination = models.CharField(
        default="12-12-12",
        null=False,
        blank=False,
        max_length=255,
        validators=[validate_combination_format],
    )
    good_student = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.name}'
    def add_subject(self,subject_id,):
        num_subjects = self.subjects.count()
        subject = Subject.objects.get(id=subject_id)
        if num_subjects<8:
            self.subjects.add(subject)
        else:
            raise Exception('This students class schedule is full!')
    def remove_subject(self,subject_id):
        subject = Subject.objects.get(id=subject_id)
        num_subjects = self.subjects.count()
        if(num_subjects>0):
            self.subjects.remove(subject)
        else:
            raise Exception('This students class schedule is empty!')
        
class Subject(models.Model):
    subject_name = models.TextField(null=False,blank=False,unique=True,validators = [validate_subject_format])
    professor = models.TextField(null =False, blank=False,default = 'Mr cahan',validators = [validate_professor_name])
    students = models.ManyToManyField(Student,related_name='subjects')

    def __repr__(self):
        return f'{self.subject_name} - {self.professor} - {self.students.count()}'
    
    def add_student(self,student_id):
        student = Student.objects.get(id=student_id)
        student_count = self.students.count()
        if student_count < 31:
            self.students.add(student)
        else:
            raise Exception('This subject is full!')
    
    def drop_a_student(self,student_id):
        student = Student.objects.get(id=student_id)
        student_count = self.students.count()
        if student_count>0:
            self.students.remove(student)
        else:
            raise Exception('This subject is empty!')

class Grade(models.Model):
    grade = models.DecimalField(null=False,blank=False,default=100, validators = [v.MinValueValidator(0),v.MaxValueValidator(100)], max_digits = 5,decimal_places =2)
    a_subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
