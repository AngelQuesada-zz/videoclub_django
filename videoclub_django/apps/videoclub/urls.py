
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.contrib.staticfiles.urls import static

from apps.videoclub.views import *

urlpatterns = [
    path(
        '',
        VideoclubIndex.as_view(),
        name='vista_index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

