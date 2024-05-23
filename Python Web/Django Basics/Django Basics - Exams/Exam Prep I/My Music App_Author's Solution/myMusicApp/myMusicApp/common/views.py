from django.shortcuts import render, redirect

from myMusicApp.album.models import Album
from myMusicApp.core.utils import get_profile
from myMusicApp.user_profile.forms import CreateProfileForm


# Create your views here.
def index(request):
    profile = get_profile()
    albums = Album.objects.all()
    context = {
        'user': profile,
        'albums': albums,
    }
    if profile:
        return render(request, 'common/home-with-profile.html', context)

    form = CreateProfileForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('index')

    context['form'] = form
    return render(request, 'common/home-no-profile.html', context)