from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from .models import task

# Create your views here.

def LogOut(request):
    logout(request)
    return redirect('login')

class loginview(LoginView):
    template_name = 'Main/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks')
    
class register(FormView):
    template_name = 'Main/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        # Save the user
        user = form.save()
        
        if user is not None:
            login(self.request, user)
        
        return super().form_valid(form)

class tasklist(LoginRequiredMixin, ListView):
    model = task
    context_object_name = 'tasks'

class taskdetail(LoginRequiredMixin, DetailView):
    model = task
    context_object_name = 'task'
    template_name = 'Main/task.html'

class taskcreate(LoginRequiredMixin, CreateView):
    model = task
    template_name = 'Main/taskform.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class taskupdate(LoginRequiredMixin, UpdateView):
    model = task
    template_name = 'Main/taskform.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class taskdelete(LoginRequiredMixin, DeleteView):
    model = task
    template_name = 'Main/taskdelete.html'
    context_object_name = 'tasks'
    success_url = reverse_lazy('tasks')
    
    
# def index(request):
#     context = {
        
#     }
#     return render(request, "", context)
