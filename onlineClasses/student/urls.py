from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.StudentList.as_view()),
        url(r'^(?P<openid>[a-zA-Z_-]+)/$', views.StudentDetail.as_view())
        ]


