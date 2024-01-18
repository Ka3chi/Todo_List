from django.urls import path
from .views import tasklist, taskdetail
from .models import task

urlpatterns = [
    path('', tasklist.as_view(), name='task'),
    path('task/<int:pk>/', taskdetail.as_view(), name='task'),
]