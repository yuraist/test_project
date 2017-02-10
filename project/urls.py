# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^', include('base.urls')),

    url(r'^admin/', admin.site.urls),
]
