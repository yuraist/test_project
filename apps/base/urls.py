# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from django.conf.urls import url

from base import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^get/$', views.GetTasksView.as_view(), name='get_tasks'),
    url(r'^get_all_tasks/$', views.GetAllTasksView.as_view(), name='get_all_tasks'),
    url(r'^get_open_tasks/$', views.GetOpenTasksView.as_view(), name='get_open_tasks'),
    url(r'^get_finished_tasks/$', views.GetFinishedTasksView.as_view(), name='get_finished_tasks'),
    url(r'^get_in_progress_tasks/$', views.GetInProgressTasksView.as_view(), name='get_in_progress_tasks'),
    url(r'^accept_task/$', views.AcceptTaskView.as_view(), name='accept_task'),
    url(r'^finish_task/$', views.FinishTaskView.as_view(), name='finish_task'),
]
