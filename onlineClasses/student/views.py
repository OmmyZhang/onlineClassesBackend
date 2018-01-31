from django.shortcuts import render
from .models import Student, StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from course.models import CourseRecord
from getid.views import session2openid

class StudentList(APIView):
    def get(self, request, format=None):
        students = Student.objects.all()
        ser = StudentSerializer(students, many=True)

        return Response(ser.data)

class StudentDetail(APIView):
    def get(self, request, ms, format=None):

        openid = session2openid(ms)
        if openid == None:
            return Response({"error":"No session, login first"},
                    status=status.HTTP_400_BAD_REQUEST)
        #print(openid)
        if Student.objects.filter(openid=openid).exists():
            un = Student.objects.get(openid=openid).username
            rec = [{
                "course_name" :r.course_name,
                "process" : r.process
                } 
                    for r in CourseRecord.objects.filter(openid=openid)
            ]
        else:
            un = ""
            rec = []
        
        return Response({'username':un,'record':rec})
    
    def post(self, request, ms, format=None):
        
        openid = session2openid(ms)
        if openid == None:
            return Response({"error":"No session, login first"},
                    status=status.HTTP_400_BAD_REQUEST)
        #print(openid)
        if Student.objects.filter(openid=openid).exists():
            return Response({"error":"openid registed"},
                    status=status.HTTP_400_BAD_REQUEST)
       

        stu = Student(
                openid=openid,
                username=request.data['username']
                )
        stu.save()
        return Response(status=status.HTTP_201_CREATED)
