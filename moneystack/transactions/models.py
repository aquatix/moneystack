"""
Models of moneystack project
"""
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    """
    Base model with common properties.
    """
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
        ordering = ('-date_created', )

    def __unicode__(self):
        return 'BaseModel created at {0}'.format(self.date_created)


class MutationsUpload(BaseModel):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='uploads/')


class Project(BaseModel):
    """
    Account that can be shared by multiple users. Can contain multiple banking accounts.
    """
    title = models.CharField(max_length=255, blank=False)
    #users


class Account(BaseModel):
    """
    Banking account
    """
    project = models.ForeignKey(Project, related_name='account', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    accountcode = models.TextField(max_length=40, blank=False,\
            help_text='Account number, like an IBAN code: NLkk bbbb cccc cccc cc')

    @property
    def total(self):
        amount = 0
        for transaction in self.transactions.all():
            amount = amount + transaction.real_amount
        return amount


class Transaction(BaseModel):
    """
    A single transaction in an account
    """
    date = models.DateTimeField()
    description = models.TextField()
    account = models.ForeignKey(Account, related_name='transactions', on_delete=models.CASCADE)
    otheraccount = models.CharField(max_length=40, blank=True)
    code = models.CharField(max_length=255, blank=True)
    # withdrawal or deposit, True or False
    withdrawal = models.BooleanField(default=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    mutation_kind = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)

    @property
    def real_amount(self):
        if withdrawal:
            return -1 * amount
        else:
            return amount


class PaymentParty(BaseModel):
    """
    A vendor, person or whatever (think supermarket, pizzeria, bank
    """
    title = models.CharField(max_length=255)
    #hash?
    #lebenstein distance thingee?
    #regexp?
