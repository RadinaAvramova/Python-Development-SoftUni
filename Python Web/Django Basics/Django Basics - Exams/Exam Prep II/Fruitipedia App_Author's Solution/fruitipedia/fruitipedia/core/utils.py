from fruitipedia.fruit.models import Fruit
from fruitipedia.user_profile.models import Profile


def get_profile():
    return Profile.objects.first()


def get_all_fruits():
    return Fruit.objects.all() if Fruit.objects.all() else None
