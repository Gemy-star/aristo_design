from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static

urlpatterns = [
    # Internationalization URLs for language switching
    path('i18n/', include('django.conf.urls.i18n')),
]

# Adding internationalized URLs to the urlpatterns
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),  # Admin URL
    path('', include('main.urls')),  # Your main application URLs
)

# For serving static and media files during development (when DEBUG is True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
