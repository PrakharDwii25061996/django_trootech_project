from rest_framework import serializers
from .models import Playlist


class PlaylistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Playlist
        fields = ['uuid', 'name', 'tracks', 'image']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.tracks = validated_data.get('tracks')
        instance.image = validated_data.get('image')
        instance.save()
        return instance

    def create(self, validated_data):
        tracks = validated_data.get('tracks')
        playlist = Playlist.objects.create(
            name=validated_data.get('name'),
            tracks=tracks,
            image=validated_data.get('image')
        )
        return playlist
