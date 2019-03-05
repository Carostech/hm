from django import forms
from django.contrib.auth.forms import UserCreationForm

from hotelweb.models import JobTitle, JobShift, User, Staff


class JobTitleForm(forms.ModelForm):
    class Meta:
        model = JobTitle
        fields = ('job_title',)


class JobShiftForm(forms.ModelForm):
    class Meta:
        model = JobShift
        fields = ('job_shift', 'shift_start_time', 'shift_end_time')


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'id_number', 'gender', 'password1', 'password2')


class StaffForm(forms.ModelForm):
  class Meta:
    model = Staff
    fields = ('staff_id', 'staff_job_title', 'staff_job_shift')
