from django.db import models
from django.core.exceptions import ValidationError
from rest_framework import permissions
import os


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class WorkType(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Photos(models.Model):
    photo = models.ImageField(upload_to='Const_photos', null=True)


class Const_projects(models.Model):
    images = models.ManyToManyField(Photos)
    plane = models.FileField(upload_to='plane_img')
    name = models.CharField(max_length=10000, null=True)
    workType = models.ForeignKey(WorkType, on_delete=models.CASCADE, null=True, related_name='projects')
    type = models.CharField(max_length=10000, null=True)
    date = models.IntegerField(null=True)
    square = models.CharField(max_length=1000, null=True)
    place = models.CharField(max_length=1000, null=True)
    status = models.CharField(max_length=20, null=True)
    team = models.CharField(max_length=10000, null=True)

    def __str__(self):
        return self.name