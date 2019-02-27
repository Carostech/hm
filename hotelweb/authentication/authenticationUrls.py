from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import authenticationViews

urlpatterns = [
    path('register/', authenticationViews.user_register, name='user_register'),
    path('login/', authenticationViews.user_login, name='user_login'),
    path('logout/', authenticationViews.user_logout, name='user_logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)