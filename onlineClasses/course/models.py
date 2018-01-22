from django.db import models
from rest_framework import serializers

class CourseRecord(models.Model):
    openid = models.CharField(max_length=127)
    course_name = models.CharField(max_length=127)
    process = models.IntegerField(default=0)

class CRSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRecord
        fields = ('openid', 'course_name', 'process')

