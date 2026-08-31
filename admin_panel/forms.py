from django import forms
from django.conf import settings
from django.core.mail import send_mail
from .models import Artist, Album, Track
from playlist.models import Playlist


class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = '__all__'
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "biography": forms.Textarea(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(
                attrs={"class": "form-control"}
             ),
        }

    def get_form_name(self):
    	return f'Artist'

    def sent_email(self):
        artist_name = self.cleaned_data.get('name')
        artist_email = self.cleaned_data.get('email')

        title = "Successfully Registered"
        message = f"""
        Congratulations {artist_name},
               You have successfully Registered to this company.
               Now, you are ready for further process.
               Our company provide Many Services 
        """

        try:
            send_mail(
                title,
                message,
                settings.EMAIL_HOST_USER,
                [artist_email],
                fail_silently=False,
            )
        except Exception as e:
            print('something wrong')


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "artist": forms.Select(attrs={"class": "form-control"}),
            "release_date": forms.SelectDateWidget(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(
                attrs={"class": "form-control"}
             ),
        }

    def get_form_name(self):
    	return f'Album'


class TrackForm(forms.ModelForm):

    class Meta:
        model = Track
        fields = '__all__'
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "album": forms.Select(attrs={"class": "form-control"}),
            "order": forms.NumberInput(attrs={"class": "form-control"}),
            "duration": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "image": forms.ClearableFileInput(
                attrs={"class": "form-control"}
             ),
        }

    def get_form_name(self):
    	return f'Track'


class PlaylistForm(forms.ModelForm):

    class Meta:
        model = Playlist
        fields = '__all__'
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "tracks": forms.Select(attrs={"class": "form-control"}),
        }

    def get_form_name(self):
        return f'Playlist'
