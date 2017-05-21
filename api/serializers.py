from rest_framework import serializers
from rest_framework.reverse import reverse

from api.models import Note, NoteContent


class NoteSerializer(serializers.ModelSerializer):
    note_contents = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = ('id', 'title', 'description', 'note_contents')

    def get_note_contents(self, obj):
        """
        Custom method to get the urls of the note contents for a note
        :param obj: 
        :return: 
        """
        request = self.context.get('request')
        note_contents = obj.note_contents.all()
        note_contents_urls = [
            request.build_absolute_uri(
                reverse('note-content-detail', kwargs={'note_id': obj.id, 'note_content_id': note_content.id}))
            for note_content in note_contents]

        return note_contents_urls


class NoteContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NoteContent
        fields = ('id', 'note', 'content', 'done')
