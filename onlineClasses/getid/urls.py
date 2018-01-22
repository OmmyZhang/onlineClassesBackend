from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.Openid.as_view())
        ]


