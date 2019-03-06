from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages

from .staffForms import JobTitleForm, JobShiftForm, UserForm, StaffForm
from hotelweb.models import JobTitle, JobShift, Staff


@login_required
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

    return render(request, 'hotelweb/staff/jobTitle/add_job_title.html', context)


@login_required
def all_job_title(request):
    job_titles = JobTitle.objects.select_related().filter(job_title_status=1)

    context = {
        'job_titles': job_titles
    }
    return render(request, 'hotelweb/staff/jobTitle/all_job_titles.html', context)


@login_required
def job_title_details(request, job_title_id):
    job_title = get_object_or_404(JobTitle, id=job_title_id)
    staff = Staff.objects.filter(staff_job_title=job_title, staff_user__status=1)

    context = {
        'job_title': job_title,
        'staff': staff
    }

    return render(request, 'hotelweb/staff/jobTitle/job_title_details.html', context)


@login_required
def update_job_title(request, job_title_id):
    job_title = JobTitle.objects.get(id=job_title_id)

    if request.method == "POST":
        form = JobTitleForm(request.POST, instance=job_title)

        if form.is_valid():
            job_title = form.save()
            messages.success(request, 'Job title was updated successfully')
            return redirect('update_job_title', job_title_id=job_title_id)

    else:
        form = JobTitleForm(instance=job_title)

    context = {
        'job_title': job_title,
        'form': form
    }

    return render(request, 'hotelweb/staff/jobTitle/update_job_title.html', context)


@login_required
def deactivate_job_title(request, job_title_id):
    job_title = JobTitle.objects.get(id=job_title_id)
    job_title.job_title_status = 0
    job_title.save(update_fields=['job_title_status'])
    messages.add_message(request, messages.SUCCESS, 'Job title removed successfully')
    return redirect('all_job_titles')


@login_required
def add_job_shift(request):
    if request.method == "POST":
        form = JobShiftForm(request.POST)
        if form.is_valid():
            job_shift = form.save(commit=False)
            job_shift.created_by = request.user
            job_shift.save()
            messages.success(request, 'Job shift was added successfully')
            return redirect('add_job_shift')

    else:
        form = JobShiftForm()

    context = {
        'form': form
    }

    return render(request, 'hotelweb/staff/jobShift/add_job_shift.html', context)


@login_required
def all_job_shifts(request):
    job_shifts = JobShift.objects.filter(job_shift_status=1)

    context = {
        'job_shifts': job_shifts
    }

    return render(request, 'hotelweb/staff/jobShift/all_job_shifts.html', context)


@login_required
def update_job_shift(request, job_shift_id):
    job_shift = JobShift.objects.get(id=job_shift_id)

    if request.method == "POST":
        form = JobShiftForm(request.POST, instance=job_shift)

        if form.is_valid():
            job_shift = form.save()
            messages.success(request, 'Job shift was updated successfully')
            return redirect('update_job_shift', job_shift_id=job_shift_id)

    else:
        form = JobShiftForm(instance=job_shift)

    context = {
        'job_shift': job_shift,
        'form': form
    }

    return render(request, 'hotelweb/staff/jobShift/update_job_shift.html', context)


@login_required
def add_staff(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        staff_form = StaffForm(request.POST)

        if user_form.is_valid() and staff_form.is_valid():
            # Save general user details
            user = user_form.save(commit=False)
            user.is_staff = True
            user.save()

            # Save staff specific details
            staff = staff_form.save(commit=False)
            staff.staff_user = user
            staff.staff_created_by = request.user

            # Success message
            messages.success(request, 'The staff has been successfully created')
            return redirect('add_staff')

    else:
        user_form = UserForm()
        staff_form = StaffForm()

    context = {
        'user_form': user_form,
        'staff_form': staff_form
    }

    return render(request, 'hotelweb/staff/add_staff.html', context)




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