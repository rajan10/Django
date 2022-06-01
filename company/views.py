from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Employee, Company
from .forms import  EmployeeForm
from django.views.generic import View
from django.contrib import messages

# Create your views here.
def index(request):
    return HttpResponse("hello world!")


def create_employee(request):
    if request.method=='GET':
        form=EmployeeForm()
        context={}
        context['form']=form
        return render(request, template_name="create_employee.html", context=context)
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            company = Company.objects.all()[0]
            print(company)
            full_name =form.cleaned_data['full_name']
            designation = form.cleaned_data['designation']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            employee=Employee(company= company,full_name=full_name,designation=designation,email=email,phone=phone)
            employee.save()
            return redirect('read_employee')


def read_employee(request):
    employees=Employee.objects.all()
    return render(request,"read_employee.html", {'employees':employees})

def update_employee(request,id):
    employee=get_object_or_404(Employee, pk=id)
    if request.method=='GET':
        data={'full_name':employee.full_name,'designation':employee.designation,'email':employee.email,'phone':employee.phone}
        form =EmployeeForm(data)
        context={}
        context['form']=form
        return render(request,template_name='update_employee.html', context=context)
    if request.method == 'POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            employee.full_name = form.cleaned_data['full_name']
            employee.designation=form.cleaned_data['designation']
            employee.email=form.cleaned_data['email']
            employee.phone=form.cleaned_data['phone']
            employee.save(update_fields=['full_name','designation','email','phone'])
            return redirect('read_employee')
def delete_employee(request, id):
    employee=Employee.objects.filter(pk=id)
    employee.delete()
    return redirect('read_employee')