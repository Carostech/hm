from django.db import models
from django.utils import timezone


# Create your models here.
# course categories.
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    id_number = models.CharField(max_length=50, null=False)
    gender = models.CharField(max_length=10, null=False)
    has_baby = models.CharField(max_length=10, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.user_id


class Rooms(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_number = models.CharField(max_length=20, null=False)
    room_type = models.CharField(max_length=50, null=False)
    floor = models.CharField(max_length=10, null=False)
    cleaning_status = models.CharField(max_length=10, null=False)
    status = models.CharField(max_length=50, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.room_id


class Workers(models.Model):
    worker_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    id_number = models.CharField(max_length=50, null=False)
    gender = models.CharField(max_length=10, null=False)
    staff_id = models.CharField(max_length=100, null=True)
    role = models.CharField(max_length=100, null=False)
    shift = models.CharField(max_length=100, null=True)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.worker_id


class Cleaning(models.Model):
    cleaning_id = models.AutoField(primary_key=True)
    worker_id = models.CharField(max_length=50, null=False)
    facility_type = models.CharField(max_length=50, null=False)
    facility_id = models.CharField(max_length=50, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.cleaning_id


class Facilities(models.Model):
    facility_id = models.AutoField(primary_key=True)
    facility_number = models.CharField(max_length=50, null=False)
    facility_name = models.CharField(max_length=50, null=False)
    floor = models.CharField(max_length=50, null=False)
    facility_type = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=50, null=False)
    capacity = models.CharField(max_length=50, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.facility_id


class Vehicles(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    number_plate = models.CharField(max_length=100, null=False)
    owner_type = models.CharField(max_length=100, null=False)
    user_id = models.CharField(max_length=100, null=False, help_text="User ID can be worker_id or user_id")
    parking_id = models.CharField(max_length=100, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.vehicle_id


class Ratings(models.Model):
    rating_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100, null=False)
    rating = models.CharField(max_length=100, null=False)
    comment = models.CharField(max_length=100, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.rating_id


class Parking(models.Model):
    parking_id = models.AutoField(primary_key=True)
    parking_location = models.CharField(max_length=100, null=False)
    parking_slot_number = models.CharField(max_length=100, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.parking_id


class Events(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    venue = models.CharField(max_length=100, null=False)
    type = models.CharField(max_length=100, null=False)
    start_date = models.DateTimeField(default=timezone.now())
    end_date = models.DateField(default=timezone.now())
    time = models.CharField(max_length=100, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.event_id


class Chats(models.Model):
    chat_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100, null=False)
    message = models.CharField(max_length=700, null=True)
    chat_type = models.CharField(max_length=100, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.chat_id


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100, null=False)
    start_date = models.DateTimeField(default=timezone.now())
    end_date = models.DateField(default=timezone.now())
    facility_type = models.CharField(max_length=50, null=False)
    facility_id = models.CharField(max_length=50, null=False)
    hotel_id = models.CharField(max_length=50, null=False)
    status = models.CharField(max_length=50, null=False)
    confirmation_number = models.CharField(max_length=100, null=False)
    package_id = models.CharField(max_length=100, null=False)
    booking_date = models.CharField(max_length=100, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.booking_id


class Requests(models.Model):
    request_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=50, null=False)
    user_type_id = models.CharField(max_length=50, null=False)
    request_type_id = models.CharField(max_length=50, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.request_id


class UserType(models.Model):
    user_type_id = models.AutoField(primary_key=True)
    user_type = models.CharField(max_length=50, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.user_type_id


class RequestType(models.Model):
    request_type_id = models.AutoField(primary_key=True)
    request_type = models.CharField(max_length=50, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.request_type_id


class Alerts(models.Model):
    alert_id = models.AutoField(primary_key=True)
    alert_type_id = models.CharField(max_length=50, null=False)
    message = models.CharField(max_length=700, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.alert_id


class AlertType(models.Model):
    alert_type_id = models.AutoField(primary_key=True)
    alert_type_name = models.CharField(max_length=50, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.alert_type_id


class Food(models.Model):
    food_id = models.AutoField(primary_key=True)
    food_type = models.CharField(max_length=50, null=False)
    name = models.CharField(max_length=50, null=False)
    quantity = models.CharField(max_length=50, null=False)
    metric = models.CharField(max_length=50, null=False, help_text="can be Grams, Kg, Lb")
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.food_id


class Drink(models.Model):
    drink_id = models.AutoField(primary_key=True)
    drink_type = models.CharField(max_length=50, null=False)
    name = models.CharField(max_length=50, null=False)
    quantity = models.CharField(max_length=50, null=False, help_text="can be in Litres, Boxes, Pieces")
    metric = models.CharField(max_length=50, null=False, help_text="can be Grams, Kg, Lb")
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.drink_id


class Commodity(models.Model):
    commodity_id = models.AutoField(primary_key=True)
    commodity_type = models.CharField(max_length=50, null=False)
    name = models.CharField(max_length=50, null=False)
    quantity = models.CharField(max_length=50, null=False)
    metric = models.CharField(max_length=50, null=False, help_text="can be Grams, Kg, Lb")
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.commodity_id


class Suppliers(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=50, null=False)
    supply_type = models.CharField(max_length=50, null=False)
    supply_item = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.supplier_id


class Supplies(models.Model):
    supply_id = models.AutoField(primary_key=True)
    item_id = models.CharField(max_length=50, null=False)
    item_type = models.CharField(max_length=50, null=False, help_text="Can be food, drink or commodity")
    supplier_id = models.CharField(max_length=50, null=False)
    quantity = models.CharField(max_length=50, null=False)
    cost = models.CharField(max_length=50, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.supply_id


class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100, null=False)
    quantity = models.CharField(max_length=100, null=False)
    status = models.IntegerField(max_length=2, null=False)
    status_time = models.DateTimeField(default=timezone.now())
    meal_time = models.CharField(max_length=100, null=False, help_text="Can be breakfast, lunch or dinner")
    cost = models.CharField(max_length=100, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.menu_id


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_time = models.DateTimeField(default=timezone.now())
    order_status = models.IntegerField(max_length=2, null=False)
    paid = models.IntegerField(max_length=2, null=False)
    created_by = models.IntegerField(max_length=2, null=False, default=0)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.order_id


class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=100, null=False)
    menu_id = models.CharField(max_length=100, null=False)
    quantity = models.CharField(max_length=100, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.order_item_id


class UserTrackingMovements(models.Model):
    tracking_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100, null=False)
    facility_id = models.CharField(max_length=100, null=False)
    facility_type = models.CharField(max_length=100, null=False)
    status = models.CharField(max_length=100, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.tracking_id


class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    hotel_name = models.CharField(max_length=100, null=False)
    hotel_ranking = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100, null=False)
    package = models.CharField(max_length=100, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.hotel_id


class Packages(models.Model):
    package_id = models.AutoField(primary_key=True)
    package_name = models.CharField(max_length=100, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.package_id


class Laundry(models.Model):
    laundry_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100, null=False)
    total_laundry_costs = models.CharField(max_length=100, null=False)
    status = models.CharField(max_length=100, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.laundry_id


class LaundryItems(models.Model):
    laundry_item_id = models.AutoField(primary_key=True)
    cloth_type = models.CharField(max_length=100, null=False)
    cloth_quantity = models.IntegerField(null=False)


class LaundryType(models.Model):
    laundry_item_id = models.AutoField(primary_key=True)
    clothe_type = models.CharField(max_length=100, null=False)
    cost = models.CharField(max_length=100, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.laundry_item_id


class Guests(models.Model):
    guest_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    id_number = models.CharField(max_length=50, null=False)
    gender = models.CharField(max_length=10, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.guest_id


class DispatchStock(models.Model):
    dispatch_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100, null=False)
    worker_id = models.CharField(max_length=100, null=False)
    facility_id = models.EmailField(max_length=100, null=False)
    quantity = models.CharField(max_length=50, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.dispatch_id


class RoomType(models.Model):
    room_type_id = models.AutoField(primary_key=True)
    room_type = models.CharField(max_length=50, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.room_type_id


class FacilityType(models.Model):
    facility_type_id = models.AutoField(primary_key=True)
    facility_type = models.CharField(max_length=50, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.facility_type_id


# Views definitions
class ArrivalView(models.Model):
    class Meta:
        managed = False
        db_table = 'ArrivalsView'


class DepartureView(models.Model):
    class Meta:
        managed = False
        db_table = 'DeparturesView'


class BookingSummaryView(models.Model):
    class Meta:
        managed = False
        db_table = 'BookingSummaryView'


class TodayBookingView(models.Model):
    class Meta:
        managed = False
        db_table = 'TodayBookingView'


class CancellationView(models.Model):
    class Meta:
        managed = False
        db_table = 'CancellationView'


class OverBookingView(models.Model):
    class Meta:
        managed = False
        db_table = 'OverBookingsView'


class RoomsOccupiedView(models.Model):
    class Meta:
        managed = False
        db_table = 'RoomsOccupiedView'


class InhouseGuestView(models.Model):
    class Meta:
        managed = False
        db_table = 'InhouseGuestsView'


class MostUsedFacilityView(models.Model):
    class Meta:
        managed = False
        db_table = 'MostUsedFacilityView'


class LeastUsedFacilityView(models.Model):
    class Meta:
        managed = False
        db_table = 'LeastUsedFacilityView'


class AllOrdersListView(models.Model):
    class Meta:
        managed = False
        db_table = 'AllOrdersListView'


class CleaningFacilityView(models.Model):
    class Meta:
        managed = False
        db_table = 'CleaningFacilityView'


class CleaningRoomView(models.Model):
    class Meta:
        managed = False
        db_table = 'cleaningRoomView'
