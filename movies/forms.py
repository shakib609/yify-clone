from django import forms

from .models import DownloadLink, Comment


CHOICES = [
    ('720p.BluRay', '720p.BluRay'),
    ('1080p.BluRay', '1080p.BluRay'),
    ('720p.WEBRip', '720p.WEBRip'),
    ('1080p.WEBRip', '1080p.WEBRip'),
]


class DownloadLinkForm(forms.ModelForm):
    quality = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = DownloadLink
        fields = '__all__'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text', )