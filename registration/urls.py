from django.conf.urls import url, include
from . import views
from django.contrib.auth import urls


urlpatterns = [
    url(r'^$', views.index),
    url(r'profile/',views.userProfile),
    url(r'signup/',views.signup)
]