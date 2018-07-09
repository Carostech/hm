from rest_framework import viewsets
from hotelweb.models import Users, Rooms, Workers, Cleaning, Facilities, Vehicles, Ratings, Parking, Events, Chats, \
    Booking, Requests, UserType, RequestType, Alerts, AlertType, Food, Drink, Commodity, Suppliers, Supplies, Menu, \
    Orders, OrderItem, UserTrackingMovements, Hotel
from hotelapi.serializers import UsersSerializers, RoomsSerializer, WorkersSerializer, CleaningSerializer, \
    FacilitiesSerializer, VehiclesSerializer, RatingsSerializer, ParkingSerializer, EventsSerializer, ChatsSerializer, \
    BookingSerializer, RequestsSerializer, UserTypeSerializer, RequestTypeSerializer, AlertsSerializer, \
    AlertTypeSerializer, FoodSerializer, DrinkSerializer, CommoditySerializer, SuppliersSerializer, SuppliesSerializer, MenuSerializer, \
    OrdersSerializer, OrderItemSerializer, UserTrackingMovementsSerializer, HotelSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers


class RoomsViewSet(viewsets.ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer


class WorkersViewSet(viewsets.ModelViewSet):
    queryset = Workers.objects.all()
    serializer_class = WorkersSerializer


class CleaningViewSet(viewsets.ModelViewSet):
    queryset = Cleaning.objects.all()
    serializer_class = CleaningSerializer


class FacilitiesViewSet(viewsets.ModelViewSet):
    queryset = Facilities.objects.all()
    serializer_class =FacilitiesSerializer


class VehiclesViewSet(viewsets.ModelViewSet):
    queryset = Vehicles.objects.all()
    serializer_class =VehiclesSerializer


class RatingsViewSet(viewsets.ModelViewSet):
    queryset = Ratings.objects.all()
    serializer_class =RatingsSerializer


class ParkingViewSet(viewsets.ModelViewSet):
    queryset = Parking.objects.all()
    serializer_class =ParkingSerializer


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class =EventsSerializer


class ChatsViewSet(viewsets.ModelViewSet):
    queryset = Chats.objects.all()
    serializer_class =ChatsSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class =BookingSerializer


class RequestsViewSet(viewsets.ModelViewSet):
    queryset = Requests.objects.all()
    serializer_class =RequestsSerializer


class UserTypeViewSet(viewsets.ModelViewSet):
    queryset = UserType.objects.all()
    serializer_class =UserTypeSerializer


class RequestTypeViewSet(viewsets.ModelViewSet):
    queryset = RequestType.objects.all()
    serializer_class =RequestTypeSerializer


class AlertsViewSet(viewsets.ModelViewSet):
    queryset = Alerts.objects.all()
    serializer_class =AlertsSerializer


class AlertTypeViewSet(viewsets.ModelViewSet):
    queryset = AlertType.objects.all()
    serializer_class =AlertTypeSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class =FoodSerializer


class DrinkViewSet(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class =DrinkSerializer


class CommodityViewSet(viewsets.ModelViewSet):
    queryset = Commodity.objects.all()
    serializer_class =CommoditySerializer


class SuppliersViewSet(viewsets.ModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class =SuppliersSerializer


class SuppliesViewSet(viewsets.ModelViewSet):
    queryset = Supplies.objects.all()
    serializer_class =SuppliesSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class =MenuSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class =OrdersSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class =OrderItemSerializer


class UserTrackingMovementsViewSet(viewsets.ModelViewSet):
    queryset = UserTrackingMovements.objects.all()
    serializer_class =UserTrackingMovementsSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer