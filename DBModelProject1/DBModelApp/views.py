from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from DBModelApp.models import Employee
from DBModelApp.models import Company


# Create your views here.
def empdata(request):
    emplist=Employee.objects.all()
    dict1={'emplist':emplist}
    return render(request,'DBModelApp/emp.html',context=dict1);
def compdata(request):
    complist=Company.objects.all()
    dict1={'complist':complist}
    return render(request,'DBModelApp/comp.html',context=dict1);