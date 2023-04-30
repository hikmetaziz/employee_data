#urls.py #myapp
from django.urls import path
from . import views



urlpatterns = [
    path('',views.index,name='index'),
    path('specific',views.specific,name='specific'),

    path('showEmployeeSheet',views.showEmployeeSheet,name='showEmployeeSheet'),

    path('createEmployee',views.createEmployee,name="createEmployee"),

    path('editEmployeeShet/<int:employee_id>/',views.editEmployeeSheet,name="editEmployeeSheet"),

    path('editEmployee',views.editEmployee,name="editEmployee"),
  
    path('deleteEmployee/<int:employee_id>',views.deleteEmployee,name='deleteEmployee')
]
