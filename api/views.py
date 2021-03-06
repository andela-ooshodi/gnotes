# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Note, NoteContent

from .serializers import NoteSerializer, NoteContentSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given note.

    list:
    Return a list of all the existing notes.

    create:
    Create a new note instance.
    
    partial_update:
    Partially update a note instance.
    
    update:
    Update a note instance. Note that every put is made to be a partial update
    
    delete:
    Delete a note instance.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    # force all put request to be a partial update
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()


class NoteContentViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given note content.

    list:
    Return a list of all the existing note contents.

    create:
    Create a new note content instance.
    
    partial_update:
    Partially update a note content instance.
    
    update:
    Update a note content instance. Note that every put is made to be a partial update
    
    delete:
    Delete a note content instance.
    """
    serializer_class = NoteContentSerializer
    lookup_field = 'note_content_id'

    def get_queryset(self):
        note_id = self.kwargs.get('note_id')
        queryset = NoteContent.objects.filter(note=note_id)

        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        filter = {'pk': self.kwargs.get(self.lookup_field)}

        obj = get_object_or_404(queryset, **filter)
        return obj

    # force all put request to be a partial update
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()
