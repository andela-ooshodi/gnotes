from django.test import TestCase

from api.models import Note, NoteContent


class GNoteModelsTest(TestCase):

    def setUp(self):
        self.note = Note.objects.create(title='Paris Trip', description='Things to do in Paris')
        self.note_content = NoteContent.objects.create(note=self.note, content='Visit Eiffel Tower', done=False)

    def test_can_retrieve_note(self):
        note = Note.objects.get(id=self.note.id)
        self.assertEqual(note.title, self.note.title)
        self.assertEqual(note.description, self.note.description)

    def test_can_retrieve_note_content(self):
        note_contents = NoteContent.objects.filter(note=self.note)
        self.assertEqual(note_contents.count(), 1)
        self.assertEqual(note_contents[0].note, self.note_content.note)
        self.assertEqual(note_contents[0].content, self.note_content.content)
        self.assertEqual(note_contents[0].done, self.note_content.done)
