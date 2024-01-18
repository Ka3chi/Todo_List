from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import task

# Create your views here.
class tasklist(ListView):
    model = task
    context_object_name = 'task'

class taskdetail(DetailView):
    model = task
    context_object_name = 'task'