from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,documents_root=settings.STATIC_ROOT)
    #urlpatterns = urlpatterns + static(settings.MEDIA_URL,doucoment_root=settings.MEDIA_ROOT)
