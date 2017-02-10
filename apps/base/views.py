# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView


__all__ = (
    b'IndexView',
    b'GetTasksView',
)


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'base/index.html'


class GetTasksView(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        items = []
        return JsonResponse({'items': items})
