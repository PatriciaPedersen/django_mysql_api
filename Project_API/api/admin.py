from django.contrib import admin
from .models import Company
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'website', 'foundation')
    search_fields = ('name', 'website', 'foundation')

admin.site.register(Company,CompanyAdmin)