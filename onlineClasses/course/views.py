from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,status
from .models import CourseRecord, CRSerializer, File
from django.http import HttpResponseRedirect
import datetime

class CRList(generics.ListCreateAPIView):
    queryset = CourseRecord.objects.all()
    serializer_class = CRSerializer


    #    ic = request.data.get('invite_code')
    #    if not InviteCode.objects.filter(code = ic).exists():
    #        return Response({'info':'invalid invite code'},
    #                status=status.HTTP_400_BAD_REQUEST)
    #    
    #    InviteCode.objects.filter(code = ic).delete()

class FileData(APIView):
    def get(self, request, filename, format=None):
        openid = request.GET['openid']

        if File.objects.filter(name=filename).exists():
            f = File.objects.filter(name=filename)[0]
            if(CourseRecord.objects.filter(course_name=f.course_name, openid=openid).exists) \
                    and (f.available_time < datetime.datetime.now()):
                return HttpResponseRedirect('/media/'+filename)
            else:
                return Response({'info':'unavailable'},
                        status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'info':'unavailable'},
                    status=status.HTTP_400_BAD_REQUEST)

