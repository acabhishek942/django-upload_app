# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = patterns('',
                      (r'^home/', include('handle_upload.upload_app.urls')),
                       # Just for ease of use.
                      (r'^$', RedirectView.as_view(url='/home/list/')),
                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
