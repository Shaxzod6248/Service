from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .serializers import Const_projectsSerializer, WorkTypeSerializer, Const_servicesSerializer
from projects.models import Const_projects, WorkType
from services.models import Const_services


class WorkTypeAPIView(APIView):
    def get(self, request):
        worktype = WorkType.objects.all()
        serializer = WorkTypeSerializer(worktype, context={'request': request}, many=True)
        return Response(serializer.data)


class WorkTypeDetail(APIView):
    def get_object(self, pk):
        try:
            return WorkType.objects.get(id=pk)
        except WorkType.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        worktype = self.get_object(pk)
        serializer = WorkTypeSerializer(worktype)
        return Response(serializer.data)

    def put(self, request, pk):
        worktype = self.get_object(pk)
        serializer = WorkTypeSerializer(worktype, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        worktype = self.get_object(pk)
        serializer = WorkTypeSerializer(worktype, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        worktype = self.get_object(pk)
        worktype.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Const_projectsAPIView(APIView):
    def get(self, request):
        projects = Const_projects.objects.all()
        serializer = Const_projectsSerializer(projects, context={'request': request}, many=True)
        return Response(serializer.data)

class Const_projectsDetail(APIView):
    def get_object(self, pk):
        try:
            return Const_projects.objects.get(id=pk)
        except Const_projects.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        projects = self.get_object(pk)
        serializer = Const_projectsSerializer(projects)
        return Response(serializer.data)

    def put(self, request, pk):
        projects = self.get_object(pk)
        serializer = Const_projectsSerializer(projects, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        projects = self.get_object(pk)
        serializer = Const_projectsSerializer(projects, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        projects = self.get_object(pk)
        projects.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Const_servicesAPIView(APIView):
    def get(self, request):
        services = Const_services.objects.all()
        serializer = Const_servicesSerializer(services, context={'request': request}, many=True)
        return Response(serializer.data)

class Const_servicesDetail(APIView):
    def get_object(self, pk):
        try:
            return Const_services.objects.get(id=pk)
        except Const_projects.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        services = self.get_object(pk)
        serializer = Const_servicesSerializer(services)
        return Response(serializer.data)

    def put(self, request, pk):
        services = self.get_object(pk)
        serializer = Const_servicesSerializer(services, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        services = self.get_object(pk)
        serializer = Const_servicesSerializer(services, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        services = self.get_object(pk)
        services.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)