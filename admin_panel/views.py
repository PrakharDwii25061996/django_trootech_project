from django.shortcuts import render
from django.http import HttpResponse

from .models import Artist, Album, Track
from .forms import ArtistForm, AlbumForm, TrackForm, PlaylistForm
from playlist.models import Playlist

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, ListView, DetailView


def index(request):
	return render(request, 'admin_panel/index.html', {})


class ArtistFormView(FormView):
    template_name = "admin_panel/form_view.html"
    form_class = ArtistForm
    success_url = reverse_lazy("artist_list")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ArtistListView(ListView):
    model = Artist
    template_name = "admin_panel/artist_list.html"
    context_object_name = "artist_list"


class ArtistEditFormView(UpdateView):
    model = Artist
    form_class = ArtistForm
    template_name = "admin_panel/form_view.html"
    success_url = reverse_lazy("artist_list")
    slug_url_kwarg = "int"
    slug_field = "pk"


class ArtistDeleteView(DeleteView):

    def get(self, request, *args, **kwargs):
        status = get_object_or_404(Artist, pk=kwargs.get("pk"))
        status.delete()
        return redirect("artist_list")


class AlbumFormView(FormView):
    template_name = "admin_panel/form_view.html"
    form_class = AlbumForm
    success_url = reverse_lazy("album_list")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AlbumListView(ListView):
    model = Album
    template_name = "admin_panel/album_list.html"
    context_object_name = "album_list"


class AlbumEditFormView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = "admin_panel/form_view.html"
    success_url = reverse_lazy("album_list")
    slug_url_kwarg = "int"
    slug_field = "pk"


class AlbumDeleteView(DeleteView):

    def get(self, request, *args, **kwargs):
        album = get_object_or_404(Album, pk=kwargs.get("pk"))
        album.delete()
        return redirect("album_list")


class TrackFormView(FormView):
    template_name = "admin_panel/form_view.html"
    form_class = TrackForm
    success_url = reverse_lazy("track_list")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class TrackListView(ListView):
    model = Track
    template_name = "admin_panel/track_list.html"
    context_object_name = "track_list"


class TrackEditFormView(UpdateView):
    model = Track
    form_class = TrackForm
    template_name = "admin_panel/form_view.html"
    success_url = reverse_lazy("track_list")
    slug_url_kwarg = "int"
    slug_field = "pk"


class TrackDeleteView(DeleteView):

    def get(self, request, *args, **kwargs):
        track = get_object_or_404(Track, pk=kwargs.get("pk"))
        track.delete()
        return redirect("track_list")


class PlaylistFormView(FormView):
    template_name = "admin_panel/form_view.html"
    form_class = PlaylistForm
    success_url = reverse_lazy("playlist_list")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PlaylistListView(ListView):
    model = Playlist
    template_name = "admin_panel/playlist.html"
    context_object_name = "playlist_list"

    def get(self, request, *args, **kwargs):
        playlist = Playlist.objects.all()
        return render(
            request,
            'admin_panel/playlist.html',
            {'playlist': playlist}
        )


class PlaylistEditFormView(UpdateView):
    model = Playlist
    form_class = PlaylistForm
    template_name = "admin_panel/form_view.html"
    success_url = reverse_lazy("playlist_list")
    slug_url_kwarg = "int"
    slug_field = "pk"


class PlaylistDeleteView(DeleteView):

    def get(self, request, *args, **kwargs):
        playlist = get_object_or_404(Playlist, pk=kwargs.get("pk"))
        playlist.delete()
        return redirect("playlist_list")
