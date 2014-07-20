# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('handle_upload.upload_app.views',
                       url(r'^list/$', 'list', name='list'),
                       )
