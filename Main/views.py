from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import task

# Create your views here.
class tasklist(ListView):
    model = task
    context_object_name = 'tasks'

class taskdetail(DetailView):
    model = task
    context_object_name = 'task'
    template_name = 'Main/task.html'

class taskcreate(CreateView):
    model = task
    template_name = 'Main/taskform.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class taskupdate(UpdateView):
    model = task
    template_name = 'Main/taskform.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class taskdelete(DeleteView):
    model = task
    template_name = 'Main/taskdelete.html'
    context_object_name = 'tasks'
    success_url = reverse_lazy('tasks')
