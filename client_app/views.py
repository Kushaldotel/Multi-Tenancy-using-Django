from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
# Create your views here.

def index(request):
    return HttpResponse(f"Hello, world. You're at the polls index.{request.tenant}")


def create_employee(request,name):
    emp = Employee(name=name)
    emp.save()
    return HttpResponse(f"Employee created successfully for {request.tenant}")