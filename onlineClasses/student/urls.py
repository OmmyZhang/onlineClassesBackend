from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.StudentList.as_view()),
        url(r'^(?P<ms>[A-Z0-9]+)/$', views.StudentDetail.as_view())
        ]


