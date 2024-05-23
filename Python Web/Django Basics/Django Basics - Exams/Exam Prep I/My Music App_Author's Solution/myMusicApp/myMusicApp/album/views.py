from django.shortcuts import render, redirect, get_object_or_404

from myMusicApp.album.forms import CreateAlbumForm, EditAlbumForm, DeleteAlbumForm
from myMusicApp.album.models import Album
from myMusicApp.core.utils import get_profile


# Create your views here.
def add_album(request):

    form = CreateAlbumForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.instance.owner_id = get_profile().pk
        form.save()
        return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'album/album-add.html', context)


def details_album(request, pk):
    album = get_object_or_404(Album, pk=pk)

    context = {
        'album': album
    }
    return render(request, 'album/album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)

    form = EditAlbumForm(instance=album)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'album/album-edit.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)

    form = DeleteAlbumForm(instance=album)
    if request.method == 'POST':
        album.delete()
        return redirect('index')

    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'album/album-delete.html', context)