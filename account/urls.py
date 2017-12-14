
#-*- coding: utf-8 -*-

from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    # url(r'^login/$', views.user_login, name = 'user_login'),
    url(r'^login/$', auth_views.login, name = 'user_login'),
    url(r'^new_login/$', auth_views.login, {"template_name": "account/login.html"}),
    url(r'^logout/$', auth_views.logout, {"template_name": "account/logout.html"}, name = "user_logout"),
    # url(r'^logout/$', auth_views.logout, name = "user_logout"),
]