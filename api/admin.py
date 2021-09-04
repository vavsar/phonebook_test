from django.contrib import admin

from .models import Organisation, Employee, UserEditor


class OrganisationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
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


class UserEditorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'organisation',
    )


admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(UserEditor, UserEditorAdmin)
