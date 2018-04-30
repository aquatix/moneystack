"""
Django admin stuff for moneystack
"""
from django.contrib import admin

from .models import Account, Project


class ProjectAdmin(admin.ModelAdmin):
    """
    Edit projects
    """
    list_display = ('title',)


class AccountAdmin(admin.ModelAdmin):
    """
    Edit accounts
    """
    list_display = ('title',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Account, AccountAdmin)
