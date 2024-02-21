from django.urls import path
from .views import tasklist, taskdetail, taskcreate, taskupdate, taskdelete, loginview, register
from . import views

urlpatterns = [
    path('login/', loginview.as_view(), name='login'),
    path('register/', register.as_view(), name='register'),
    path('logout/', views.LogOut, name='logout'),
    path('', tasklist.as_view(), name='tasks'),
    path('task/<int:pk>/', taskdetail.as_view(), name='task'),
    path('task-create/', taskcreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', taskupdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', taskdelete.as_view(), name='task-delete'),
]