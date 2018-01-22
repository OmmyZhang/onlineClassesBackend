from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import CourseRecord, CRSerializer

class CRList(generics.ListCreateAPIView):
    queryset = CourseRecord.objects.all()
    serializer_class = CRSerializer

class FileData(APIView):
    def get(self, request, format=None):
        
        return Response("ok")

