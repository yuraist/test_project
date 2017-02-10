# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from django.conf.urls import url

from base import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^get/$', views.GetTasksView.as_view(), name='get_tasks'),
]
