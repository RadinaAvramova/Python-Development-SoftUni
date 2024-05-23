from django.shortcuts import render, redirect

from fruitipedia.core.utils import get_profile, get_all_fruits
from fruitipedia.fruit.forms import CreateFruitForm, EditFruitForm, DeleteFruitForm
from fruitipedia.fruit.models import Fruit


def index(request):
    profile = get_profile()
    context = {'profile': profile}
    return render(request, template_name='index.html', context=context)


def dashboard(request):
    profile = get_profile()
    fruits = get_all_fruits()
    context = {
        'profile': profile,
        'fruits': fruits,
    }
    return render(request, 'dashboard.html', context)


def add_fruit(request):
    profile = get_profile()
    form = CreateFruitForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.owner = profile
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'fruit/create-fruit.html', context)


def details_fruit(request, fruit_id):
    fruit = Fruit.objects.get(id=fruit_id)
    profile = get_profile()

    context = {
        'fruit': fruit,
        'profile': profile,

    }
    return render(request, 'fruit/details-fruit.html', context)


def edit_fruit(request, fruit_id):
    fruit = Fruit.objects.get(id=fruit_id)
    profile = get_profile()

    form = EditFruitForm(instance=fruit)
    if request.method == 'POST':
        form = EditFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'fruit': fruit,
        'form': form,
        'profile': profile,
    }
    return render(request, 'fruit/edit-fruit.html', context)


def delete_fruit(request, fruit_id):
    profile = get_profile()
    fruit = Fruit.objects.get(id=fruit_id)

    form = DeleteFruitForm(instance=fruit)
    if request.method == 'POST':
        fruit.delete()
        return redirect('dashboard')

    context = {
        'fruit': fruit,
        'form': form,
        'profile': profile,
    }
    return render(request, 'fruit/delete-fruit.html', context)