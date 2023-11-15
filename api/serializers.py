from rest_framework import serializers
from projects.models import *
from services.models import Const_services


class Const_projectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Const_projects
        fields = '__all__'


class WorkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkType
        fields = '__all__'


class Const_servicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Const_services
        fields = '__all__'