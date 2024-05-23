from django.urls import path, include

from myMusicApp.album.views import add_album, delete_album, details_album, edit_album

urlpatterns = [
    path('add/', add_album, name='add album'),
    path('<int:pk>/', include([
        path('details/', details_album, name='details album'),
        path('edit/', edit_album, name='edit album'),
        path('delete/', delete_album, name='delete album'),
    ]))

]