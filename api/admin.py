from django.contrib import admin
from api.models import Company,Employee
# Register your models here..

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')
    search_fields=('name',)  #for search_bar
    
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','company')
    list_filter=('company',) #for search_bar

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)