from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.CRList.as_view()),
        url(r'^file/(?P<filename>[^/]+\.[\w]+)/$', views.FileData.as_view())
        ]


