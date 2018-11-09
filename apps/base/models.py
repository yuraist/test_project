# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from django.conf import settings
from django.db import models


class TaskStatus(object):

    OPEN = 1
    IN_PROGRESS = 20
    FINISHED = 30

    CHOICES = (
        (OPEN, 'OPEN'),
        (IN_PROGRESS, 'IN_PROGRESS'),
        (FINISHED, 'FINISHED'),
    )


class Task(models.Model):

    text = models.TextField()
    link = models.URLField(max_length=1024)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tasks', null=True, blank=True)
    status = models.SmallIntegerField(choices=TaskStatus.CHOICES, default=TaskStatus.OPEN)

    def json_representation(self):
        json = {
            'text': self.text,
            'link': self.link,
            'price': self.price,
            'status': self.status,
        }

        if self.assignee is not None:
            json['assignee'] = {
                'id': self.assignee.id,
                'username': self.assignee.username,
            }

        return json
