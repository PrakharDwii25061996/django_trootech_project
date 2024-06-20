from django.db import models
import uuid

from admin_panel.models import Track


class Playlist(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200)
    tracks = models.ForeignKey(
        Track, related_name='playlist_tracks', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
