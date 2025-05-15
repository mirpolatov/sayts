from django.urls import path
from apps.views import home, artist, kliplar, konsert, musiqa, toplamlar

urlpatterns = [
    path('', home, name='home'),
    path('artist', artist, name='artist'),
    path('kliplar', kliplar, name='kliplar'),
    path('konsert', konsert, name='konsert'),
    path('musiqa', musiqa, name='musiqa'),
    path('toplamlar', toplamlar, name='toplamlar'),

    ]