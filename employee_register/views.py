from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee

#view table function
def employee_list(request):
    context = {"employee_list":Employee.objects.all()}
    return render(request,"employee_register/employee_list.html",context)

#insert and update function
def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:  
            #get blank form
            form = EmployeeForm()
        else:
            #get filled form for update     
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            #post for for inserting records
            form = EmployeeForm(request.POST)
        else:
            #post for for updating records
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee) #instance for editing else new record will be created
        if form.is_valid():
            form.save()
        return redirect('/employee/list')

#delete function
def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')
