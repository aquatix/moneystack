"""
Django admin stuff for moneystack
"""
from django.contrib import admin

from .models import Account, Project, Transaction


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


class TransactionAdmin(admin.ModelAdmin):
    """
    Edit transactions
    """
    list_display = ('date', 'account', 'otheraccount', 'code', 'amount', 'payment_reference',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)
