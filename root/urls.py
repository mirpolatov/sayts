from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from apps import apps
from root import settings

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel uchun marshrut
    path('', include('apps.urls')),  # Ilovalaringizdagi marshrutlar
]

# Statik va media fayllarni ishlash
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)