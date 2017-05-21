from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from api.models import Note, NoteContent


class ApiViewsTest(APITestCase):
    def setUp(self):
        self.note = Note.objects.create(title='Paris Trip', description='Things to do in Paris')
        self.note_content = NoteContent.objects.create(note=self.note, content='Visit Eiffel Tower', done=False)

    def test_can_create_note(self):
        url = reverse('note-list')
        data = {'title': 'Google Note', 'description': 'Copy of google keep'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_can_get_notes(self):
        url = reverse('note-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_retrieve_note(self):
        url = reverse('note-detail', kwargs={'pk': self.note.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_update_note(self):
        url = reverse('note-detail', kwargs={'pk': self.note.id})
        data = {'description': 'Things i\'ld love to do in Paris'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_note(self):
        url = reverse('note-detail', kwargs={'pk': self.note.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_can_create_note_content(self):
        url = reverse('note-content-list', kwargs={'note_id': self.note.id})
        note_url = reverse('note-detail', kwargs={'pk': self.note.id})
        data = {'note': note_url, 'content': 'Copy of google keep'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_can_get_note_contents(self):
        url = reverse('note-content-list', kwargs={'note_id': self.note.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_retrieve_note_content(self):
        url = reverse('note-content-detail', kwargs={'note_id': self.note.id, 'note_content_id': self.note_content.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_update_note_content(self):
        url = reverse('note-content-detail', kwargs={'note_id': self.note.id, 'note_content_id': self.note_content.id})
        data = {'content': 'Things i\'ld love to do in Paris'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_note_content(self):
        url = reverse('note-content-detail', kwargs={'note_id': self.note.id, 'note_content_id': self.note_content.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

