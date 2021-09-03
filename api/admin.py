from django.contrib import admin

from .models import Organisation, Employee


class OrganisationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'owner',
    )


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'creator',
        'private_phone',
        'work_phone',
        'organisation'
    )


admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Employee, EmployeeAdmin)
