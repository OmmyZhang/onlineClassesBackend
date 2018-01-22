from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class Process(APIView):
    def post(self, request, format=None):
        body = request.data

        return Response("ok")

class FileData(APIView):
    def get(self, request, format=None):
        
        return Response("ok")

