from django.conf.urls import url, include
from rest_framework import routers

from .views import NoteViewSet, NoteContentViewSet

# register our v1 api URL pattern
v1_router = routers.DefaultRouter()
v1_router.register(r'notes', NoteViewSet, base_name='note')
v1_router.register(r'notes/(?P<note_id>[0-9]+)/note-contents', NoteContentViewSet, base_name='note-content')

urlpatterns = [
    url(r'^v1/', include(v1_router.urls)),
]
