from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,status
from .models import CourseRecord, CRSerializer, File
from django.http import HttpResponseRedirect
from student.models import InviteCode
from getid.views import session2openid
import datetime

class CRList(APIView):
    def get(self, request, format=None):
        cr = CourseRecord.objects.all()
        ser = CRSerializer(cr, many=True)
        return Response(ser.data)
    
    def post(self, request, format=None):
        data = request.data
        cn = data['course_name']
        ms = data['my_session']
        ps = data['process']
        ic = data.get('invite_code')

        openid = session2openid(ms)
        if openid == None:
            return Response({"error":"No session, login first"},
                    status=status.HTTP_400_BAD_REQUEST)
        
        if CourseRecord.objects.filter(course_name=cn, openid=openid):
            cr = CourseRecord.objects.get(course_name=cn, openid=openid)
            cr.process = ps
            cr.save()
            return Response()
        
        print(ic)
        if not InviteCode.objects.filter(code = ic).exists():
            return Response({'info':'invalid invite code'},
                    status=status.HTTP_400_BAD_REQUEST)
        
        InviteCode.objects.filter(code = ic).delete()

        cr = CourseRecord(
                openid=openid,
                course_name=cn,
                process=ps
                )
        cr.save()
        return Response(status=status.HTTP_201_CREATED)


class FileData(APIView):
    def get(self, request, filename, format=None):
        #openid = request.GET['openid']
        
        ms = request.GET['my_session']
        openid = session2openid(ms)
        if openid == None:
            return Response({"error":"No session, login first"},
                    status=status.HTTP_400_BAD_REQUEST)
        

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

