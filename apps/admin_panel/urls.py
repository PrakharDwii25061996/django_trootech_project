from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Artist url path
    path('artist/', views.ArtistFormView.as_view(), name='artist_form'),
    path('artist/list/', views.ArtistListView.as_view(), name='artist_list'),
    path('artist/edit/<int:pk>/', views.ArtistEditFormView.as_view(), name='artist_edit_form'),
    path('artist/del/<int:pk>/', views.ArtistDeleteView.as_view(), name='artist_delete'),

    # Album url path
    path('album/', views.AlbumFormView.as_view(), name='album_form'),
    path('album/list/', views.AlbumListView.as_view(), name='album_list'),
    path('album/edit/<int:pk>/', views.AlbumEditFormView.as_view(), name='album_edit_form'),
    path('album/del/<int:pk>/', views.AlbumDeleteView.as_view(), name='album_delete'),

    # Track url path
    path('track/', views.TrackFormView.as_view(), name='track_form'),
    path('track/list/', views.TrackListView.as_view(), name='track_list'),
    path('track/edit/<int:pk>/', views.TrackEditFormView.as_view(), name='track_edit_form'),
    path('track/del/<int:pk>/', views.TrackDeleteView.as_view(), name='track_delete'),

    # Playlist url path
    path('playlist/', views.PlaylistFormView.as_view(), name='playlist_form'),
    path('playlist/list/', views.PlaylistListView.as_view(), name='playlist_list'),
    path('playlist/edit/<int:pk>/', views.PlaylistEditFormView.as_view(), name='playlist_edit_form'),
    path('playlist/del/<int:pk>/', views.PlaylistDeleteView.as_view(), name='playlist_delete'),
]