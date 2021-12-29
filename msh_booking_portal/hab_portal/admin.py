from django.contrib import admin
from .models import HABModel
from import_export.admin import ImportExportModelAdmin

class HABModelAdmin(ImportExportModelAdmin):
    search_fields = ['name', 'user__user__username', 'roll_number', 'hostel']
    list_display = ('email','name','roll_number','programme','vaccination_status')
# Register your models here.
admin.site.register(HABModel, HABModelAdmin)
