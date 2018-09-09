from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from . import views

urlpatterns = [
                path('register/', views.user_register, name='user_register'),
                path('login/', views.user_login, name='user_login'),
                path('logout/', views.user_logout, name='user_logout'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
