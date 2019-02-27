from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import staffViews

urlpatterns = [
    path('staff/add/', staffViews.add_staff, name='add_staff'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)