from django import forms

from hotelweb.models import FacilityType


class FacilityTypeForm(forms.ModelForm):
    class Meta:
        model = FacilityType
        fields = ('facility_type_name',)
