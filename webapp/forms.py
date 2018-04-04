from django import forms
from .models import *
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']


class VideosForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['name', 'description', 'category', 'video']


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'artist', 'genre', 'logo']


class SongsForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['name', 'album_i', 'song']


class ImagesForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'img']


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'src', 'description']


class MessagesForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Message
        fields = ['message']


class NotificationForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Notification
        fields = ['body', 'send_to']

