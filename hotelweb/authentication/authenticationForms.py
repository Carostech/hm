from django.contrib.auth.forms import UserCreationForm
from django import forms

from hotelweb.models import User


#class CreateUserForm(UserCreationForm):

 #   class Meta:
  #      model = User
   #     fields = ('email', 'first_name', 'last_name', 'phone', 'job_title', 'password1', 'password2')


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())