from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render, redirect


from hotelweb.authentication.authenticationForms import LoginForm
from hotelweb.models import User


#def user_register(request):
 #   if request.method == "POST":
  #      form = CreateUserForm(request.POST)
   #     if form.is_valid():
    #        user = form.save(commit=False)
     #       user.created_on = timezone.now()
      #      user.save()
       #     messages.success(request, 'Registered successfully')
        #    return redirect('user_register')
    #else:
     #   form = CreateUserForm()
    #return render(request, 'hotelweb/authentication/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                try:
                    user = User.objects.get(email=email)
                    form.add_error('password', "invalid password")
                except User.DoesNotExist:
                    form.add_error('email', "invalid email address")

    else:
        form = LoginForm
    return render(request, 'hotelweb/authentication/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('user_login')