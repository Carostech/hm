from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages

from .staffForms import JobTitleForm, StaffForm
from hotelweb.models import JobTitle


def add_job_title(request):
    if request.method == "POST":
        form = JobTitleForm(request.POST)
        if form.is_valid():
            job_title = form.save(commit=False)
            job_title.job_created_by = request.user
            job_title.save()
            messages.success(request, 'Job title was created successfully')
            return redirect('add_job_title')

    else:
        form = JobTitleForm()

    context = {
        'form': form
    }

    return render(request, 'hotelweb/staff/add_job_title.html', context)


def all_job_title(request):
    job_titles = JobTitle.objects.filter(job_title_status=1)

    context = {
        'job_titles': job_titles
    }
    return render(request, 'hotelweb/staff/all_job_titles.html', context)


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