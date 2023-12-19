from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='client_index'),
    path('create_employee/<name>/', views.create_employee, name='create_employee'),
]