from django.db import models
from rest_framework import serializers

class Student(models.Model):
    openid = models.CharField(max_length=127)
    username = models.CharField(max_length=127)
    def __str__(self):
        return self.openid + ' : ' + self.username

class InviteCode(models.Model):
    code = models.CharField(max_length=127)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('openid', 'username')
