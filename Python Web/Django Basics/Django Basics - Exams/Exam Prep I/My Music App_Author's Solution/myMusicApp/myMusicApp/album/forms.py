from django import forms

from myMusicApp.album.models import Album


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields[fieldname].widget.attrs['placeholder'] = self.fields[fieldname].label


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('owner',)


class DeleteAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
