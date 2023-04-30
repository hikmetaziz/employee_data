from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee

def index(request):
    employees = Employee.objects.all()
    return render(request, "myapp/index.html", {'employees': employees})

def specific(request):
    return HttpResponse('number')

def showEmployeeSheet(request):
    return render(request, 'myapp/employeeSheet.html')

def createEmployee(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        job = request.POST.get('job')
        salary = request.POST.get('salary')
        employee = Employee(name=name, email=email, job=job, salary=salary)
        employee.save()
        return redirect('index')
    return redirect('index')


def editEmployeeSheet(request,employee_id):
    employee = Employee.objects.get(pk=employee_id)
    return render(request,'myapp/editEmployeeSheet.html',{'employee':employee})


def editEmployee(request):
    if request.method == "POST":
       id = request.POST.get('id')
       name = request.POST.get('name')
       email = request.POST.get('email')
       job = request.POST.get('job')
       salary = request.POST.get('salary')
       #get old info
       employee = Employee.objects.get(pk=id)
       employee.name = name
       employee.email = email
       employee.job = job
       employee.save()
       return redirect('index')
    return redirect('index')

    
def deleteEmployee(request,employee_id):
    employee = Employee.objects.get(pk=employee_id)
    employee.delete()
    return redirect('index')
