from django.shortcuts import render
from django.urls import path
from apps.views import home, artist, kliplar, konsert, musiqa, toplamlar
from django.shortcuts import render

urlpatterns = [
    path('', home, name='home'),
    path('artist', artist, name='artist'),
    path('kliplar', kliplar, name='kliplar'),
    path('konsert', konsert, name='konsert'),
    path('musiqa', musiqa, name='musiqa'),
    path('toplamlar', toplamlar, name='toplamlar'),

]


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


handler404 = custom_404_view
