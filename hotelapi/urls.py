"""Hotel API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include
from rest_framework import routers
from hotelapi import views

# registering API endpoints
router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'rooms', views.RoomsViewSet)
# router.register(r'cleaning', views.CleaningViewSet)
# router.register(r'facilities', views.FacilitiesViewSet)
# router.register(r'vehicles', views.VehiclesViewSet)
# router.register(r'ratings', views.RatingsViewSet)
# router.register(r'parking', views.ParkingViewSet)
# router.register(r'events', views.EventsViewSet)
# router.register(r'chats', views.ChatsViewSet)
# router.register(r'booking', views.BookingViewSet)
# router.register(r'requests', views.RequestsViewSet)
# router.register(r'usertype', views.UserTypeViewSet)
# router.register(r'requesttype', views.RequestTypeViewSet)
# router.register(r'alerts', views.AlertsViewSet)
# router.register(r'alerttype', views.AlertTypeViewSet)
# router.register(r'food', views.FoodViewSet)
# router.register(r'drink', views.DrinkViewSet)
# router.register(r'commodity', views.CommodityViewSet)
# router.register(r'suppliers', views.SuppliersViewSet)
# router.register(r'supplies', views.SuppliesViewSet)
# router.register(r'menu', views.MenuViewSet)
# router.register(r'order', views.OrderViewSet)
# router.register(r'orderitem', views.OrderItemViewSet)
# router.register(r'tracking', views.UserTrackingMovementsViewSet)
# router.register(r'hotel', views.HotelViewSet)


urlpatterns = [
    re_path(r'^', include(router.urls)),
    path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
