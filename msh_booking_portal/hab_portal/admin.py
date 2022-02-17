from django.contrib import admin
from .models import HABModel, NewHABModel, CampusReturn2022
from import_export.admin import ImportExportModelAdmin

class HABModelAdmin(ImportExportModelAdmin):
    search_fields = ['name', 'user__user__username', 'roll_number', 'hostel']
    list_display = ('name','roll_number','programme','vaccination_status')

class NewHABModelAdmin(ImportExportModelAdmin):
    search_fields = ['name', 'user__user__username', 'roll_number', 'hostel']
    list_display = ('name','roll_number','programme','vaccination_status')

class CampusReturn2022Admin(ImportExportModelAdmin):
    search_fields = ['name', 'user__user__username', 'roll_number', 'hostel']
    list_display = ('name','roll_number','programme','vaccination_status')

# Register your models here.
admin.site.register(HABModel, HABModelAdmin)
admin.site.register(NewHABModel, NewHABModelAdmin)
admin.site.register(CampusReturn2022, CampusReturn2022Admin)
