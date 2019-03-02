#from django.shortcuts import render, redirect
#from django.utils import timezone
#from django.contrib import messages

#from .staffForms import StaffForm


#def add_staff(request):
 #   if request.method == "POST":
  #      form = StaffForm(request.POST)
   #     if form.is_valid():
    #        staff = form.save(commit=False)
     #       staff.created_on = timezone.now()
      #      staff.save()
       #     messages.success(request, 'Staff Created Successfully')
        #    return redirect('add_staff')
    #else:
     #   form = StaffForm()

    #context = {
     #   'form': form
    #}
    #return render(request, 'hotelweb/staff/add_staff.html', context)