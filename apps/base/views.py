# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView
from django.db.models import Q

from .models import Task

__all__ = (
    b'IndexView',
    b'GetTasksView',
    b'GetAllTasksView',
    b'GetOpenTasksView',
    b'GetInProgressTasksView',
    b'GetFinishedTasksView',
    b'AcceptTaskView',
    b'FinishTaskView',
)


def represent_in_json_format(tasks):
    json_tasks = [task.json_representations() for task in tasks]
    json = {
        'tasks': json_tasks
    }
    return json


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'base/index.html'


class GetTasksView(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        items = []
        return JsonResponse({'items': items})


class GetAllTasksView(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        current_user = self.request.user
        query = Q(status=1) | Q(assignee=current_user)

        tasks = Task.objects.filter(query)
        json = represent_in_json_format(tasks)

        return JsonResponse(json)


class GetOpenTasksView(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        tasks = Task.objects.filter(status=1)
        json = represent_in_json_format(tasks)

        return JsonResponse(json)


class GetInProgressTasksView(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        current_user = self.request.user
        query = Q(status=20) & Q(assignee=current_user)

        tasks = Task.objects.filter(query)
        json = represent_in_json_format(tasks)

        return JsonResponse(json)


class GetFinishedTasksView(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        current_user = self.request.user
        query = Q(status=30) & Q(assignee=current_user)

        tasks = Task.objects.filter(query)
        json = represent_in_json_format(tasks)

        return JsonResponse(json)


class AcceptTaskView(LoginRequiredMixin, View):

    def put(self, *args, **kwargs):
        print('AcceptTaskView')


class FinishTaskView(LoginRequiredMixin, View):

    def put(self, *args, **kwargs):
        print('FinishTaskView')
