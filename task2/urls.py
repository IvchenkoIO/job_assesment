from django.urls import path
from . import views

urlpatterns = [
    path('task2/', views.task2, name='task2'),
]