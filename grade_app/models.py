from django.db import models
from django.core import validators as v
# Create your models here.
class Grade(models.Model):
    grade = models.DecimalField(null=False,blank=False,default=100, validators = [v.MinValueValidator(0),v.MaxValueValidator(100)], max_digits = 5,decimal_places =2)
    a_subject = models.ForeignKey('subject_app.Subject',on_delete=models.CASCADE)
    student = models.ForeignKey('student_app.Student',on_delete=models.CASCADE)
