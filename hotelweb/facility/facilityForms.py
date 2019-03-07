from django import forms

from hotelweb.models import FacilityType, Facility


class FacilityTypeForm(forms.ModelForm):
    class Meta:
        model = FacilityType
        fields = ('facility_type_name',)


class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ('facility_type', 'facility_name', 'facility_location', 'facility_capacity')
