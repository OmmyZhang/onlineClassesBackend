#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
import urllib.request
import urllib.parse
from rest_framework.views import APIView
# Create your views here.



class Openid(APIView):
    def get(self, request, format=None):
        body = request.GET

        needKey = ['appid', 'secret', 'js_code']
        data = {key: body.get(key) for key in needKey}
        data['grant_type'] = 'authorization_code'

        params = urllib.parse.urlencode(data)
        f = urllib.request.urlopen("https://api.weixin.qq.com/sns/jscode2session?%s" % params)

        json = f.read().decode('utf-8')

        return HttpResponse(json)




