"""
Django admin stuff for moneystack
"""
from django.contrib import admin
from .models import (\
    Project,
    Account)


class ProjectAdmin(admin.ModelAdmin):
    """
    Edit projects
    """
    list_display = ('name',)


class AccountAdmin(admin.ModelAdmin):
    """
    Edit accounts
    """
    list_display = ('name',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Account, AccountAdmin)
