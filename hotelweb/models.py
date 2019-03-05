from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from hashid_field import HashidAutoField

from hotelweb.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    gender_choices = (('Female', 'Female'), ('Male', 'Male'))

    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False, unique=True)
    phone = models.CharField(max_length=50, null=False)
    id_number = models.CharField(max_length=50, null=False)
    gender = models.CharField(choices=gender_choices, max_length=100, null=False)
    created_on = models.DateTimeField(null=False, default=timezone.now)
    is_staff = models.BooleanField(null=False,default=False)
    is_client = models.BooleanField(null=False, default=False)
    is_superuser = models.BooleanField(null=False, default=False)
    is_active = models.BooleanField(null=False, default=True)
    status = models.IntegerField(default=1, null=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def publish_user(self):
        self.created_on = timezone.now
        self.save()

    def __str__(self):
        return self.get_full_name()


class JobTitle(models.Model):
    id = HashidAutoField(primary_key=True)
    job_title = models.CharField(max_length=100, null=False)
    job_created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    job_created_on = models.DateTimeField(default=timezone.now)
    job_title_status = models.IntegerField(default=1)

    def __str__(self):
        return self.job_title


class JobShift(models.Model):
    job_shift = models.CharField(max_length=100, null=False)
    shift_start_time = models.TimeField(null=False)
    shift_end_time = models.TimeField(null=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now, null=False)
    job_shift_status = models.IntegerField(default=1)

    def __str__(self):
        return self.job_shift


class Staff(models.Model):
    staff_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff_user')
    staff_id = models.CharField(null=False, max_length=100)
    staff_job_title = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    staff_job_shift = models.ForeignKey(JobShift, on_delete=models.CASCADE)
    staff_created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='staff_created_by')


class Client(models.Model):
    client_user = models.OneToOneField(User, on_delete=models.CASCADE)
    client_has_baby = models.BooleanField(default=False, null=False)


class FacilityType(models.Model):
    facility_type_name = models.CharField(max_length=100, null=False)
    facility_type_status = models.IntegerField(null=False,default=1)
    facility_type_created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    facility_type_created_on = models.DateTimeField(null=False, default=timezone.now)

    def __str__(self):
        return self.facility_type_name


class Facility(models.Model):
    facility_type = models.OneToOneField(FacilityType, on_delete=models.CASCADE)
    facility_floor = models.IntegerField(null=False)
    facility_number = models.CharField(max_length=50, null=False)
    facility_cleaning_status = models.IntegerField(null=False, default=1)
    facility_created_on = models.DateTimeField(default=timezone.now, null=False)
    facility_created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    facility_status = models.IntegerField(null=False, default=1)


class RoomType(models.Model):
    room_type_name = models.CharField(null=False, max_length=100)
    room_type_status = models.IntegerField(null=False, default=1)
    room_type_created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    room_type_created_on = models.DateTimeField(null=False, default=timezone.now)


class Room(models.Model):
    room_facility = models.OneToOneField(Facility, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)


class OtherFacility(models.Model):
    facility_name = models.CharField(max_length=50, null=False)
    facility_location = models.CharField(max_length=50, null=False)
    facility_capacity = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.facility_name


class Cleaning(models.Model):
    cleaning_staff = models.ForeignKey(User, on_delete=models.CASCADE)
    cleaning_facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    cleaning_time = models.DateTimeField(default=timezone.now)


class Parking(models.Model):
    parking_location = models.CharField(max_length=100, null=False)
    parking_slot_number = models.CharField(max_length=100, null=False)
    parking_created_on = models.DateTimeField(default=timezone.now)
    parking_created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    parking_status = models.IntegerField(null=False, default=1)


class Vehicle(models.Model):
    vehicle_number_plate = models.CharField(max_length=100, null=False)
    vehicle_user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle_parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
    vehicle_created_on = models.DateTimeField(default=timezone.now)


class Rating(models.Model):
    rating_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(null=False)
    rating_comment = models.TextField(blank=True)
    rating_created_on = models.DateTimeField(default=timezone.now)


class EventType(models.Model):
    event_type_name = models.CharField(null=False, max_length=100)
    event_type_created_on = models.DateTimeField(null=False, default=timezone.now)
    event_type_created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type_status = models.IntegerField(null=False, default=1)

    def __str__(self):
        return self.event_type_name


class Event(models.Model):
    event_name = models.CharField(max_length=100, null=False)
    event_venue = models.ForeignKey(Facility, on_delete=models.CASCADE)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    event_start_date = models.DateTimeField(default=timezone.now)
    event_end_date = models.DateField(default=timezone.now)
    event_created_on = models.DateTimeField(default=timezone.now)
    event_created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Chat(models.Model):
    chat_sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_sender')
    chat_recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_receiver')
    chat_message = models.CharField(max_length=700, null=True)
    chat_type = models.CharField(max_length=100, null=False)
    chat_time = models.DateTimeField(null=False, default=timezone.now)


class Package(models.Model):
    package_name = models.CharField(max_length=100, null=False)
    package_created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    package_created_on = models.DateTimeField(default=timezone.now)
    package_status = models.IntegerField(null=False, default=1)


class Booking(models.Model):
    booking_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking_client')
    booking_facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    booking_start_date = models.DateTimeField(default=timezone.now)
    booking_end_date = models.DateField(default=timezone.now)
    booking_confirmation_number = models.CharField(max_length=100, blank=True)
    booking_package = models.ForeignKey(Package, on_delete=models.CASCADE)
    booking_created_on = models.DateTimeField(default=timezone.now)
    booking_status = models.IntegerField(null=False, default=0)


class RequestType(models.Model):
    request_type_name = models.CharField(max_length=50, null=False)
    request_type_created_on = models.DateTimeField(default=timezone.now)
    request_type_created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.request_type_name


class Request(models.Model):
    request_user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_request_type = models.ForeignKey(RequestType, models.CASCADE)
    request_created_on = models.DateTimeField(default=timezone.now)


class AlertType(models.Model):
    alert_type_name = models.CharField(null=False, max_length=100)
    alert_type_created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    alert_type_created_on = models.DateTimeField(null=False, default=timezone.now)

    def __str__(self):
        return self.alert_type_name


class Alert(models.Model):
    alert_title = models.ForeignKey(AlertType, on_delete=models.CASCADE)
    alert_message = models.TextField(null=False)
    alert_created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    alert_created_on = models.DateTimeField(default=timezone.now)


class CommodityCategory(models.Model):
    commodity_category_name = models.CharField(max_length=100, null=False)
    commodity_category_created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    commodity_category_created_on = models.DateTimeField(null=False, default=timezone.now)
    commodity_category_status = models.IntegerField(null=False, default=1)

    def __str__(self):
        return self.commodity_category_name


class CommodityType(models.Model):
    commodity_category = models.ForeignKey(CommodityCategory, on_delete=models.CASCADE)
    commodity_type_name = models.CharField(max_length=100, null=False)
    commodity_type_created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    commodity_type_created_on = models.DateTimeField(null=False, default=timezone.now)
    commodity_type_status = models.IntegerField(null=False, default=1)

    def __str__(self):
        return self.commodity_type_name


class CommodityMetric(models.Model):
    commodity_metric_name = models.CharField(max_length=100, null=False)
    commodity_metric_created_on = models.DateTimeField(null=False, default=timezone.now)
    commodity_metric_created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    commodity_metric_status = models.IntegerField(null=False, default=1)

    def __str__(self):
        return self.commodity_metric_name


class Commodity(models.Model):
    commodity_category = models.ForeignKey(CommodityCategory, on_delete=models.CASCADE)
    commodity_type = models.ForeignKey(CommodityType, on_delete=models.CASCADE)
    commodity_name = models.CharField(max_length=100, null=False)
    commodity_created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    commodity_created_on = models.DateTimeField(null=False, default=timezone.now)
    commodity_status = models.IntegerField(null=False, default=1)

    def __str__(self):
        return self.commodity_name


class SupplierType(models.Model):
    supplier_type_name = models.CharField(max_length=100, null=False)
    supplier_type_created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    supplier_type_created_on = models.DateTimeField(null=False, default=timezone.now)
    supplier_type_status = models.IntegerField(null=False, default=1)

    def __str__(self):
        return self.supplier_type_name


class Supplier(models.Model):
    supplier_full_name = models.CharField(max_length=100, null=False)
    supplier_type = models.ForeignKey(SupplierType, on_delete=models.CASCADE)
    supplier_phone = models.CharField(max_length=100, null=False)
    supplier_email = models.EmailField(max_length=100, null=False, unique=True)
    supplier_created_on = models.DateTimeField(default=timezone.now)
    supplier_created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    supplier_status = models.IntegerField(null=False, default=1)


class Supply(models.Model):
    supply_commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    supply_quantity = models.IntegerField(null=False)
    supply_metric = models.ForeignKey(CommodityMetric, on_delete=models.CASCADE)
    supply_cost = models.IntegerField(null=False)
    supply_supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    supply_created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    supply_created_on = models.DateTimeField(null=False, default=timezone.now)


class DispatchStock(models.Model):
    dispatch_commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    dispatch_quantity = models.IntegerField(null=False)
    dispatch_metric = models.ForeignKey(CommodityMetric, on_delete=models.CASCADE)
    dispatch_to_staff = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    dispatch_facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    dispatch_created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dispatcher')
    dispatch_created_on = models.DateTimeField(default=timezone.now)


class MealTime(models.Model):
    meal_time_name = models.CharField(max_length=100, null=False)
    meal_time_created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_time_created_on = models.DateTimeField(null=False, default=timezone.now)

    def __str__(self):
        return self.meal_time_name


class Menu(models.Model):
    meal_name = models.CharField(max_length=100, null=False)
    meal_time = models.ForeignKey(MealTime, on_delete=models.CASCADE)
    meal_cost = models.IntegerField(null=False)
    meal_image = models.ImageField(upload_to='media/meal/', null=True, blank=True)
    meal_created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_created_on = models.DateTimeField(default=timezone.now)
    meal_status = models.IntegerField(null=False, default=1)

    def __str__(self):
        return self.meal_name


class DayMenu(models.Model):
    day_menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    day_menu_quantity = models.IntegerField(null=False)
    day_menu_created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    day_menu_created_on = models.DateTimeField(null=False, default=timezone.now)


class Order(models.Model):
    order_created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    order_created_on = models.DateTimeField(default=timezone.now)
    order_order_status = models.IntegerField(null=False, default=0)
    order_paid = models.BooleanField(null=False, default=False)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    order_item = models.ForeignKey(DayMenu, on_delete=models.CASCADE)
    order_item_quantity = models.IntegerField(null=False, default=1)


class UserTrackingMovements(models.Model):
    user_tracking = models.ForeignKey(User, on_delete=models.CASCADE)
    user_tracking_facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    user_tracking_status = models.CharField(max_length=100, null=False)
    user_tracking_created_on = models.DateTimeField(default=timezone.now)


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100, null=False)
    hotel_ranking = models.CharField(max_length=100, null=False)
    hotel_location = models.CharField(max_length=100, null=False)
    hotel_package = models.CharField(max_length=100, null=False)
    hotel_created_on = models.DateTimeField(default=timezone.now)


class LaundryType(models.Model):
    laundry_type_cloth = models.CharField(max_length=100, null=False)
    laundry_type_cost = models.IntegerField(null=False)
    laundry_type_created_on = models.DateTimeField(default=timezone.now)
    laundry_type_created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Laundry(models.Model):
    laundry_client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='laundry_client')
    laundry_created_on = models.DateTimeField(default=timezone.now)
    laundry_created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='laundry_staff')
    laundry_status = models.IntegerField(null=False, default=0)


class LaundryItem(models.Model):
    laundry = models.ForeignKey(Laundry, on_delete=models.CASCADE)
    laundry_item_cloth = models.ForeignKey(LaundryType, on_delete=models.CASCADE)
    laundry_cloth_quantity = models.IntegerField(null=False)


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
