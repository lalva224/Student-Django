from django.db import models
from .validators import validate_professor_name,validate_subject_format
# Create your models here.
class Subject(models.Model):
    subject_name = models.TextField(null=False,blank=False,unique=True,validators = [validate_subject_format])
    professor = models.TextField(null =False, blank=False,default = 'Mr cahan',validators = [validate_professor_name])
    students = models.ManyToManyField('student_app.Student',related_name='subjects')

    def __repr__(self):
        return f'{self.subject_name} - {self.professor} - {self.students.count()}'
    
    def add_student(self,student_id):
        from student_app.models import Student

        student = Student.objects.get(id=student_id)
        student_count = self.students.count()
        if student_count < 31:
            self.students.add(student)
        else:
            raise Exception('This subject is full!')
    
    def drop_a_student(self,student_id):
        from student_app.models import Student
        student = Student.objects.get(id=student_id)
        student_count = self.students.count()
        if student_count>0:
            self.students.remove(student)
        else:
            raise Exception('This subject is empty!')
