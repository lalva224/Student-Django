# Generated by Django 5.0.3 on 2024-03-26 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0001_initial'),
        ('subject_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='students',
            field=models.ManyToManyField(null=True, related_name='subjects', to='student_app.student'),
        ),
    ]
