from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^login/$', views.Openid.as_view())
        ]


