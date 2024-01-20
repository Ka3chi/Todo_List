from django.urls import path
from .views import tasklist, taskdetail, taskcreate, taskupdate, taskdelete
from .models import task

urlpatterns = [
    path('', tasklist.as_view(), name='tasks'),
    path('task/<int:pk>/', taskdetail.as_view(), name='task'),
    path('task-create/', taskcreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', taskupdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', taskdelete.as_view(), name='task-delete'),
]