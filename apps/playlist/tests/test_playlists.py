# tests/test_playlists.py

from django.test import TestCase
from django.shortcuts import reverse
from rest_framework import status
from admin_panel.models import Album, Artist, Track
from playlist.models import Playlist


class PlaylistTestCase(TestCase):

    def setUp(self):
        self.artist = Artist.objects.create(
            name='Prakhar Dwivedi',
            biography='He is well known singer'
        )
        self.album = Album.objects.create(
            title='First Album',
            artist=self.artist,
            release_date='1996-12-23'
        )
        self.track1 = Track.objects.create(
            title='Track 1', album=self.album, order=1, duration=180
        )
        self.track2 = Track.objects.create(
            title='Track 2', album=self.album, order=1, duration=180
        )
        self.playlist = Playlist.objects.create(
            name='Test Playlist', tracks=self.track1
        )

    def test_playlist_post(self):
        url = reverse('playlist-list')  # Assuming you are using DefaultRouter
        data = {
            "name": "New Playlist",
            "tracks": self.track1.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Playlist.objects.count(), 2)
        self.assertEqual(Playlist.objects.all()[0].tracks.id, data['tracks'])

    def test_playlist_get_request(self):
        url = reverse('playlist-list')  # Assuming you are using DefaultRouter
        data = {
            "name": "Test Playlist",
            "tracks": self.track1.id
        }
        post_response = self.client.post(url, data, format='json')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Playlist.objects.count(), 2)
        self.assertEqual(Playlist.objects.all()[0].name, data['name'])

    def test_playlist_update_request(self):
        url = reverse('playlist-detail', args=[self.playlist.id])  # Assuming you are using DefaultRouter
        data = {
            "name": "New Playlist Updated",
            "tracks": self.track1.id
        }
        post_response = self.client.put(url, data, format='json', content_type='application/json')
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)
        self.playlist.refresh_from_db()
        self.assertEqual(Playlist.objects.count(), 1)
        self.assertEqual(Playlist.objects.all()[0].name, data['name'])

    def test_playlist_delete_request(self):
        url = reverse('playlist-detail', args=[self.playlist.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Playlist.objects.count(), 0)
