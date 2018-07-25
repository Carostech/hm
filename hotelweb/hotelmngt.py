from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from hotelweb.models import Workers


class WorkersList(ListView):
    model = Workers


class WorkerDetails(DetailView):
    model = Workers


class WorkerCreate(CreateView):
    model = Workers
    fields = ['worker_id', 'name', 'phone', 'email', 'id_number', 'gender', 'staff_id', 'role', 'shift']
    success_url = reverse_lazy('worker_list')


class WorkerUpdate(UpdateView):
    model = Workers
    fields = ['worker_id', 'name', 'phone', 'email', 'id_number', 'gender', 'staff_id', 'role', 'shift']
    success_url = reverse_lazy('worker_list')


class WorkerDelete(DeleteView):
    model = Workers
    success_url = reverse_lazy('worker_list')