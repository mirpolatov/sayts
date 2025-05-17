from django.shortcuts import render

from apps.models import Asosiy, Konsert, Kliplar, Toplamlar, AsosiyBolimIjorchi


def home(request):
    hero_images = Asosiy.objects.all()
    kliplars = Kliplar.objects.all().order_by('-id')
    toplam = Toplamlar.objects.all()
    asosiy = AsosiyBolimIjorchi.objects.all()
    return render(request, 'index.html',
                  {'images': hero_images, 'kliplar': kliplars, 'toplamlar': toplam, 'asosiy': asosiy})


def artist(request):
    return render(request, 'artist.html')


def kliplar(request):
    kliplars = Kliplar.objects.all()
    return render(request, 'kliplar.html', {'kliplar': kliplars})


def konsert(request):
    konsertlar = Konsert.objects.all()
    return render(request, 'konsert.html', {'konsertlar': konsertlar})


def musiqa(request):
    return render(request, 'musiqa.html')


def toplamlar(request):
    return render(request, 'toplamlar.html')
