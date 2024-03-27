from django.db import models
from django.core import validators as v
from student_app.validators import validate_combination_format,validate_name_format,validate_school_email
from subject_app.models import Subject


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
        unique=True,
        null=True,
        blank=True,
        validators=[v.MinValueValidator(1), v.MaxValueValidator(200)],
    )
    locker_combination = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        validators=[validate_combination_format],
    )
    good_student = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.name}'
    def add_subject(self,subject_id,):
        # from subject_app.models import Subject
        num_subjects = self.subjects.count()
        subject = Subject.objects.get(id=subject_id)
        if num_subjects<8:
            self.subjects.add(subject)
        else:
            raise Exception('This students class schedule is full!')
    def remove_subject(self,subject_id):
        # from subject_app.models import Subject
        subject = Subject.objects.get(id=subject_id)
        num_subjects = self.subjects.count()
        if(num_subjects>0):
            self.subjects.remove(subject)
        else:
            raise Exception('This students class schedule is empty!')
        



