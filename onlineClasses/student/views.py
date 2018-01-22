from django.shortcuts import render
from .models import Student, InviteCode, StudentSerializer
from rest_framework.response import Response
from rest_framework import status,permissions,serializers
from rest_framework.views import APIView
from course.models import CourseRecord

class StudentList(APIView):
    def post(self, request, format=None):
        ic = request.data.get('invite_code')
        if not InviteCode.objects.filter(code = ic).exists():
            return Response({'info':'invalid invite code'},
                    status=status.HTTP_400_BAD_REQUEST)
        
        InviteCode.objects.filter(code = ic).delete()
        
        ser = StudentSerializer(data=request.data)
        if(ser.is_valid()):
            ser.save()
            return Response(ser.data,
                 status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors,
                 status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        students = Student.objects.all()
        ser = StudentSerializer(students, many=True)

        return Response(ser.data)

class StudentDetail(APIView):
    def get(self, request, openid, format=None):
        try:
            stu = Student.objects.get(openid=openid)
            rec = [{
                "course_name" :r.course_name,
                "process" : r.process
                } 
                    for r in CourseRecord.objects.filter(openid=openid)
            ]
            return Response(rec)
        except Exception as e:
            return Response({"info":repr(e)},
                    status=status.HTTP_400_BAD_REQUEST)
