from django import forms

from hotelweb.models import Workers


class StaffForm(forms.ModelForm):
    class Meta:
        model = Workers
        fields = ('name', 'phone', 'email', 'id_number', 'gender', 'staff_id', 'role', 'shift')
