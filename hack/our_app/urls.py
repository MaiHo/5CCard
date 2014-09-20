# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
import django.contrib.auth.views

urlpatterns = patterns('hack.our_app.views',
    url(r'^login/$', 'login'),
    url(r'^main/$','main'),
                       )
