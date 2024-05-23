from django.shortcuts import render, redirect

from myMusicApp.album.models import Album
from myMusicApp.core.utils import get_profile
from myMusicApp.user_profile.forms import DeleteProfileForm


# Create your views here.


def details_profile(request):
    user = get_profile()
    album_count = Album.objects.filter(owner=user).count()

    context = {
        'user': user,
        'album_count': album_count,
    }
    return render(request, 'profile/profile-details.html', context)


def delete_profile(request):
    user = get_profile()

    form = DeleteProfileForm(instance=user)
    if request.method == 'POST':
        # Album.objects.all().delete()
        user.delete()
        return redirect('index')

    context = {
        'user': user,
        'form': form,
    }
    return render(request, 'profile/profile-delete.html', context)