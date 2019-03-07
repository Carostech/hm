from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .facilityForms import FacilityTypeForm, FacilityForm
from hotelweb.models import FacilityType, Facility


@login_required
def add_facility_type(request):
    if request.method == "POST":
        form = FacilityTypeForm(request.POST)
        if form.is_valid():
            facility_type = form.save(commit=False)
            facility_type.facility_type_created_by = request.user
            facility_type.save()
            messages.success(request, 'Facility type added successfully')
            return redirect('add_facility_type')

    else:
        form = FacilityTypeForm

    context = {
        'form': form
    }

    return render(request, 'hotelweb/facility/facilityType/add_facility_type.html', context)


@login_required
def all_facility_types(request):
    facility_types = FacilityType.objects.filter(facility_type_status=1)

    context = {
        'facility_types': facility_types
    }

    return render(request, 'hotelweb/facility/facilityType/all_facility_types.html', context)


@login_required
def update_facility_type(request, facility_type_id):
    facility_type = FacilityType.objects.get(id=facility_type_id)

    if request.method == "POST":
        form = FacilityTypeForm(request.POST, instance=facility_type)
        if form.is_valid():
            facility_type = form.save(commit=False)
            facility_type.save()
            messages.success(request, 'Facility type was updated successfully')
            return redirect('update_facility_type', facility_type_id = facility_type_id)

    else:
        form = FacilityTypeForm(instance=facility_type)

    context = {
        'facility_type': facility_type,
        'form': form
    }

    return render(request, 'hotelweb/facility/facilityType/update_facility_type.html', context)


@login_required
def deactivate_facility_type(request, facility_type_id):
    facility_type = FacilityType.objects.get(id=facility_type_id)
    facility_type.facility_type_status = 0
    facility_type.save(update_fields=['facility_type_status'])
    messages.add_message(request, messages.SUCCESS, 'Facility type was removed successfully')
    return redirect('all_facility_types')


@login_required
def add_facility(request):
    if request.method == "POST":
        form = FacilityForm(request.POST)
        if form.is_valid():
            facility = form.save(commit=False)
            facility.created_by = request.user
            facility.save()
            messages.success(request, 'Facility was added successfully')
            return redirect('add_facility')

    else:
        form = FacilityForm

    context = {
        'form': form
    }

    return render(request, 'hotelweb/facility/otherFacility/add_facility.html', context)


@login_required
def all_facilities(request):
    facilities = Facility.objects.filter(status=1)

    context = {
        'facilities': facilities
    }

    return render(request, 'hotelweb/facility/otherFacility/all_faciities.html', context)


@login_required
def update_facility(request, facility_id):
    facility = Facility.objects.get(id=facility_id)

    if request.method == "POST":
        form = FacilityForm(request.POST, instance=facility)

        if form.is_valid():
            facility = form.save(commit=False)
            facility.save()
            messages.success(request, 'Facility was updated successfully')
            return redirect('update_facility', facility_id=facility_id)

    else:
        form = FacilityForm(instance=facility)

    context = {
        'facility': facility,
        'form': form
    }

    return render(request, 'hotelweb/facility/otherFacility/update_facility.html', context)


@login_required
def deactivate_facility(request, facility_id):
    facility = Facility.objects.get(id=facility_id)
    facility.status = 0
    facility.save(update_fields=['status'])
    messages.add_message(request, messages.SUCCESS, 'Facility was removed successfully')
    return redirect('all_facilities')
