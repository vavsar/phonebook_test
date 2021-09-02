from django.contrib import admin

from .models import Organisation, Employee


class OrganisationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
    )


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
    )


admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Employee, EmployeeAdmin)
