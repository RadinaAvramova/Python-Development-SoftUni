from django.urls import path

from myMusicApp.common.views import index

urlpatterns = [
        path('', index, name='index'),
]