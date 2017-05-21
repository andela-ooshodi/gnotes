# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='created')
    date_modified = models.DateTimeField(auto_now=True, verbose_name='modified')

    class Meta:
        ordering = ['-date_modified']

    def __str__(self):
        """
        String representation of model
        :return:
        """
        return self.title


class NoteContent(models.Model):
    note = models.ForeignKey(Note, related_name='note_contents')
    content = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='created')
    date_modified = models.DateTimeField(auto_now=True, verbose_name='modified')

    def __str__(self):
        """
        String representation of model
        :return:
        """
        return "{}: number {} content".format(self.note, self.id)
