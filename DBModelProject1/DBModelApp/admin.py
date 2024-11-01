from multiprocessing.resource_tracker import register
from symtable import Class

from django.contrib import admin
from DBModelApp.models import Employee
from DBModelApp.models import Company

# Register your models here.
#admin.site.register(Employee)
#model(table) for admin-interface but-not mysql-table
class EmployeeAdmin(admin.ModelAdmin):
    list_display =['eno','ename','esal','eaddr'];
admin.site.register(Employee, EmployeeAdmin);


#register your models here.
#admin.site.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display=['compid','compname','noofemps','compaddr',];
admin.site.register(Company,CompanyAdmin);

