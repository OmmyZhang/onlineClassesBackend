#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
import urllib.request
import urllib.parse
from rest_framework.views import APIView
from .models import SessionRecord,AppInfo
import json,string,random,datetime
# Create your views here.

def rand_str(size=32, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def session2openid(session):
    SessionRecord.objects.filter(active_time__lte = datetime.datetime.now() - datetime.timedelta(hours=3)).delete()
    if SessionRecord.objects.filter(my_session=session).exists():
        sr = SessionRecord.objects.filter(my_session=session)[0]
        sr.active_time = datetime.datetime.now()
        sr.save()
        return sr.openid
    else:
        return None

class Openid(APIView):
    def get(self, request, format=None):
        code = request.GET['code']
        ai = AppInfo.objects.all()[0]

        data = {
                'js_code': code,
                'grant_type': 'authorization_code',
                'appid': ai.appid,
                'secret': ai.secret
                }

        params = urllib.parse.urlencode(data)
        f = urllib.request.urlopen("https://api.weixin.qq.com/sns/jscode2session?%s" % params)

        json_str = f.read().decode('utf-8')
        #print(json_str)
        rtd = json.loads(json_str)
    
        #rtd = {'session_key':'weJ7jD2v1','openid':'openid'}

        
        openid = rtd['openid']
        my_session = rand_str()

        sr = SessionRecord(
                my_session=my_session,
                openid=openid,
                active_time=datetime.datetime.now()
                )
        sr.save()

        return Response({'my_session':my_session})




