from rest_framework import serializers
from hotelweb.models import Users, Rooms, Workers, Cleaning, Facilities, Vehicles, Ratings, Parking, Events, Chats, \
    Booking, Requests, UserType, RequestType, Alerts, AlertType, Food, Drink, Commodity, Suppliers, Supplies, Menu, \
    Orders, OrderItem, UserTrackingMovements, Hotel


class UsersSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('user_id', 'name', 'phone', 'email')


class RoomsSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Rooms
        fields = ('room_id', 'room_number', 'floor', 'room_type', 'cleaning_status')


class WorkersSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Workers
        fields = ('worker_id', 'name', 'phone', 'email', 'gender', 'staff_id', 'role', 'shift')


class CleaningSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Cleaning
        fields = ('cleaning_id', 'worker_id', 'facility_type', 'facility_id')


class FacilitiesSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Facilities
        fields = ('facility_id', 'facility_number', 'floor', 'facility_type', 'location', 'capacity')


class VehiclesSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Vehicles
        fields = ('vehicle_id', 'number_plate', 'owner_type', 'user_id', 'parking_lot_number')


class RatingsSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Ratings
        fields = ('rating_id', 'user_id', 'rate', 'comment')


class ParkingSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Parking
        fields = ('parking_id', 'parking_location', 'parking_slot_number')


class EventsSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Events
        fields = ('event_id', 'name', 'venue', 'type', 'start_date', 'end_date', 'time')


class ChatsSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Chats
        fields = ('chat_id', 'user_id', 'message', 'chat_type')


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Booking
        fields = ('booking_id', 'user_id', 'start_date', 'end_date', 'facility_type','facility_id','hotel_id')


class RequestsSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Requests
        fields = ('request_id', 'user_type_id', 'user_id', 'reuqest_type_id')


class UserTypeSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = UserType
        fields = ('user_type_id', 'user_type')


class RequestTypeSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = RequestType
        fields = ('request_type_id', 'request_type')


class AlertsSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model =Alerts
        fields = ('alert_id','alert_type_id', 'message')


class AlertTypeSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = AlertType
        fields = ('alert_type_id', 'alert_type_name')


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Food
        fields = ('food_id', 'food_type', 'name', 'quantity', 'metric')


class DrinkSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Drink
        fields = ('drink_id', 'drink_type', 'name', 'quantity', 'metric')


class CommoditySerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Commodity
        fields = ('commodity_id', 'commodity_type', 'name', 'quantity', 'metric')


class SuppliersSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Suppliers
        fields = ('supplier_id', 'supplier_name', 'supplier_type', 'supplier_item', 'email','phone')


class SuppliesSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Supplies
        fields = ('supply_id', 'item_id', 'item_type', 'supplier_id', 'quantity','cost')


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Menu
        fields = ('menu_id', 'item_name', 'quantity', 'status', 'status_time','meal_time','cost')


class OrdersSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Orders
        fields = ('order_id', 'order_time', 'order_status', 'order_time', 'paid')


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = OrderItem
        fields = ('order_time_id', 'order_id', 'menu_id', 'quantity')


class UserTrackingMovementsSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model =UserTrackingMovements
        fields = ('tracking_id', 'user_id', 'location', 'facility_id', 'facility_type')


class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Hotel
        fields = ('hotel_id', 'hotel_name', 'hotel_ranking', 'location', 'package')