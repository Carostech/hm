from django.shortcuts import render
from django.views import generic
from hotelweb.models import Users, Rooms, Workers, Cleaning, Facilities, Vehicles, Ratings, Parking, Events, Chats, \
    Booking, Requests, UserType, RequestType, Alerts, AlertType, Food, Drink, Commodity, Suppliers, Supplies, Menu, \
    Orders, OrderItem, UserTrackingMovements, Hotel, ArrivalView, DepartureView, CancellationView, TodayBookingView, \
    BookingSummaryView, InhouseGuestView, OverBookingView, RoomsOccupiedView
from operator import itemgetter
from django.db.utils import DatabaseError
from django import http
import json


# Defining Generic views here.
def parse_update_params(request_params):
    result = dict()
    pk = request_params['pk']

    del request_params['pk']
    del request_params['csrfmiddlewaretoken']

    if 'name' in request_params and 'value' in request_params:
        result[request_params['name']] = request_params['value']
        del request_params['value']
        del request_params['name']

    result.update(**request_params)
    return pk, result


def _update_ajax(model_class, request):
    if request.method == 'POST' and request.is_ajax():
        pk, request_params = parse_update_params(request.POST.dict())
        model_class.objects.filter(pk=pk).update(**request_params)
        return model_class.objects.get(pk=pk)


# Listing all the arrivals in the system
class ArrivalListView(generic.ListView):
    template_name = ''
    context_object_name = 'arrival_list'
    model = ArrivalView
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArrivalListView, self).get_context_data(**kwargs)
        request_params = self.request.GET.copy()
        if 'page' in request_params:
            del request_params['page']

        request_params = filter(itemgetter(1), request_params.items())

        if request_params:
            context['request_params'] = request_params

        context['booking_id'] = self.kwargs['booking_id']
        return context

    def get_queryset(self):
        # return ArrivalView.objects.filter(arrival_id=self.kwargs['arrival_id'])
        return ArrivalView.objects.order_by('start_date')


# Listing all the departures in the system
class DepartureListView(generic.ListView):
    template_name = ''
    context_object_name = 'departure_list'
    model = DepartureView
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DepartureListView, self).get_context_data(**kwargs)
        request_params = self.request.GET.copy()
        if 'page' in request_params:
            del request_params['page']

        request_params = filter(itemgetter(1), request_params.items())

        if request_params:
            context['request_params'] = request_params

        context['booking_id'] = self.kwargs['booking_id']
        return context

    def get_queryset(self):
        return DepartureView.objects.order_by('end_date')


# Listing all the guests
class GuestListView(generic.ListView):
    template_name = ''
    context_object_name = 'guest_list'
    model = DepartureView
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GuestListView, self).get_context_data(**kwargs)
        request_params = self.request.GET.copy()
        if 'page' in request_params:
            del request_params['page']

        request_params = filter(itemgetter(1), request_params.items())

        if request_params:
            context['request_params'] = request_params

        context['guest_id'] = self.kwargs['guest_id']
        return context

    def get_queryset(self):
        return InhouseGuestView.objects.order_by('guest_id')


# Listing all the cancellations in the system
class CancellationListView(generic.ListView):
    template_name = ''
    context_object_name = 'guest_list'
    model = CancellationView
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CancellationListView, self).get_context_data(**kwargs)
        request_params = self.request.GET.copy()
        if 'page' in request_params:
            del request_params['page']

        request_params = filter(itemgetter(1), request_params.items())

        if request_params:
            context['request_params'] = request_params

        context['booking_id'] = self.kwargs['booking_id']
        return context

    def get_queryset(self):
        return CancellationView.objects.order_by('booking_date')


# Listing all the over-bookings in the system
class OverbookingListView(generic.ListView):
    template_name = ''
    context_object_name = 'guest_list'
    model = OverBookingView
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OverbookingListView, self).get_context_data(**kwargs)
        request_params = self.request.GET.copy()
        if 'page' in request_params:
            del request_params['page']

        request_params = filter(itemgetter(1), request_params.items())

        if request_params:
            context['request_params'] = request_params

        context['booking_id'] = self.kwargs['booking_id']
        return context

    def get_queryset(self):
        return OverBookingView.objects.order_by('booking_date')


# Listing all the rooms occupied
class RoomsOccupiedListView(generic.ListView):
    template_name = ''
    context_object_name = 'guest_list'
    model = RoomsOccupiedView
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RoomsOccupiedListView, self).get_context_data(**kwargs)
        request_params = self.request.GET.copy()
        if 'page' in request_params:
            del request_params['page']

        request_params = filter(itemgetter(1), request_params.items())

        if request_params:
            context['request_params'] = request_params

        context['booking_id'] = self.kwargs['booking_id']
        return context

    def get_queryset(self):
        return RoomsOccupiedView.objects.order_by('booking_date')


# creating a new booking
def add_booking_ajax(request, **kwargs):
    if request.method == 'POST':
        if request.is_ajax():
            request_params = request.POST.dict()
            print(request_params)

            try:
                booking = Booking()
                booking.user_id = request_params.get('user_id')
                booking.start_date = request_params.get('start_date')
                booking.end_date = request_params.get('end_date')
                booking.facility_type = request_params.get('facility_type')
                booking.facility_id = request_params.get('facility_id')
                booking.hotel_id = request_params.get('hotel_id')
                booking.status = request_params.get('status')
                booking.confirmation_number = request_params.get('confirmation_number')
                booking.package_id = request_params.get('package_id')
                booking.booking_date = request_params.get('booking_date')
                booking.created_on = request_params.get('created_on')
                booking.save()
                return http.HttpResponse(json.dumps({'id': booking.booking_id,
                                                     'confirmation_number': booking.confirmation_number
                                                     }), status=201)

            except DatabaseError as e:
                return http.HttpResponse(status=400, content="A problem occurred. booking not created")


# updating booking
def update_booking_ajax(request, **kwargs):
    if request.method == 'POST' and request.is_ajax():
        try:
            booking = _update_ajax(Booking, request)
            return http.HttpResponse(json.dumps({'pk': booking.booking_id,
                                                 'confirmation_number': booking.confirmation_number,
                                                 }), status=201)
        except DatabaseError as e:
            return http.HttpResponse(status=400, content='An error occurred while processing your request')
    return http.HttpResponse(status=400)


# deleting booking that was made
def delete_booking_ajax(request, **kwargs):
    if request.method == 'POST' and request.is_ajax():
        try:
            booking = Booking.objects.get(pk=request.POST.get('pk'))
            booking_cn = booking.confirmation_number
            booking.delete()
            return http.HttpResponse(
                content='booking <strong>{}</strong> has been successfully deleted'.format(booking_cn),
                status=200)
        except DatabaseError as e:
            return http.HttpResponse(status=400, content='An error occurred while processing your request')
