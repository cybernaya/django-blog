from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('admin/', admin.site.urls),
	path('ckeditor/', include('ckeditor_uploader.urls')),
	path('programming/', include('programming.urls')),
	path('networking/', include('networking.urls')),
	path('forensics/', include('forensics.urls')),
	path('cryptography/', include('cryptography.urls')),
    path('', views.index),
    path('tinymce/',include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)