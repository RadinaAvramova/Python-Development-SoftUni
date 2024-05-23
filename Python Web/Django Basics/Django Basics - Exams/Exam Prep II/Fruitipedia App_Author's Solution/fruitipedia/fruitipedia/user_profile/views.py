from django.shortcuts import render, redirect

from fruitipedia.core.utils import get_profile
from fruitipedia.fruit.models import Fruit
from fruitipedia.user_profile.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm


def create_profile(request):
    profile = get_profile()
    form = CreateProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,

    }

    return render(request, 'profile/create-profile.html', context)


def details_profile(request):
    profile = get_profile()
    post_count = Fruit.objects.filter(owner=profile).count()

    context = {
        'profile': profile,
        'post_count': post_count,

    }
    return render(request, 'profile/details-profile.html', context)


def edit_profile(request):
    profile = get_profile()

    form = EditProfileForm(instance=profile)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():

            form.save()

            return redirect('details-profile')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()

    form = DeleteProfileForm(instance=profile)
    if request.method == 'POST':
        profile.delete()
        return redirect('index')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile/delete-profile.html', context)

