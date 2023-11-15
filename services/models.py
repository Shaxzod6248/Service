from django.db import models
from django.core.exceptions import ValidationError
from rest_framework import permissions
import os


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class Const_services(models.Model):
    title = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title