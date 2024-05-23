from django.urls import path

from myMusicApp.user_profile.views import details_profile, delete_profile

urlpatterns = [
    path('details/', details_profile, name='details profile'),
    path('delete/', delete_profile, name='delete profile'),
]