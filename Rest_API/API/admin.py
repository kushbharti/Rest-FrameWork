from django.contrib import admin
from .models import Company,Employee

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','types')
    
    
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','email','position')
    list_filter = ('company',)

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)
