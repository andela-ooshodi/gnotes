# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Note, NoteContent


class NoteContentInline(admin.TabularInline):
    model = NoteContent
    extra = 1


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date_created', 'date_modified')
    inlines = [NoteContentInline]


admin.site.register(Note, NoteAdmin)
