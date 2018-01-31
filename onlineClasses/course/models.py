from django.db import models
from rest_framework import serializers

class CourseRecord(models.Model):
    openid = models.CharField(max_length=127)
    course_name = models.CharField(max_length=127)
    process = models.IntegerField(default=0)
    def __str__(self):
        return self.openid + ' --> ' + self.course_name + ' : ' + str(self.process)

class CRSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRecord
        fields = ('openid', 'course_name', 'process')


class File(models.Model):
    name = models.CharField(max_length=127)
    available_time = models.DateTimeField()
    course_name = models.CharField(max_length=127)
    def __str__(self):
        return self.name + ' in ' + self.course_name + ' @' + str(self.available_time)


