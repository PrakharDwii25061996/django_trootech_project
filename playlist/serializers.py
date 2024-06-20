from rest_framework import serializers
from .models import Playlist


class PlaylistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Playlist
        fields = ['uuid', 'name', 'tracks']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.tracks = validated_data.get('tracks')
        instance.save()
        return instance

    def create(self, validated_data):
        tracks = validated_data.get('tracks')
        playlist = Playlist.objects.create(
            name=validated_data.get('name'),
            tracks=tracks
        )
        return playlist
