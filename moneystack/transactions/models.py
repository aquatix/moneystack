"""Models of moneystack project"""
import binascii
import os
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

from .choices import *


def generate_key():
    """Generate a random string, to be used as key

    :return: string with hexadecimal representation of a 24-bit random string
    :rtype: str
    """
    return binascii.hexlify(os.urandom(24))


class BaseModel(models.Model):
    """Base model with common properties."""
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
        ordering = ('-date_created', )

    def __unicode__(self):
        return 'BaseModel created at {0}'.format(self.date_created)


class Project(BaseModel):
    """Account that can be shared by multiple users. Can contain multiple banking accounts."""
    title = models.CharField(max_length=255, blank=False)
    users = models.ManyToManyField(User)

    def __repr__(self):
        return f'Project({self.title})'

    def __str__(self):
        return f'{self.title}'


class Account(BaseModel):
    """Banking account"""
    project = models.ForeignKey(Project, related_name='account', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    accountcode = models.CharField(max_length=40, blank=False,\
            help_text='Account number, like an IBAN code: NLkk bbbb cccc cccc cc')

    secure_code = models.CharField(max_length=100, blank=False)  # Used for storing (temporary) files and such

    def __init__(self):
        super().__init__()
        # Get a random key
        self.secure_code = generate_key()

    def __repr__(self):
        return f'Account({self.id!r} {self.title!r})'

    def __str__(self):
        return f'{self.title} ({self.project})'

    @property
    def total(self):
        amount = 0
        for transaction in self.transactions.all():
            amount = amount + transaction.real_amount
        return amount


class MutationsUpload(BaseModel):
    """Uploaded transactions/mutations file (csv)"""
    account = models.ForeignKey(Account, related_name='mutationsupload', on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='uploads/')

    file_type = models.IntegerField(choices=MUTATION_FILE_TYPES, default=1)

    def __repr__(self):
        return f'MutationsUpload({self.id} {self.document.name}'

    def __str__(self):
        return f'{self.document.name}'


class Transaction(BaseModel):
    """A single transaction in an account"""
    date = models.DateTimeField()
    description = models.TextField()
    account = models.ForeignKey(Account, related_name='transactions', on_delete=models.CASCADE)
    otheraccount = models.CharField(max_length=40, blank=True)
    code = models.CharField(max_length=255, blank=True)
    # withdrawal or deposit, True or False
    withdrawal = models.BooleanField(default=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    mutation_kind_code = models.CharField(max_length=255, blank=True)
    mutation_kind = models.IntegerField(choices=MUTATION_TYPES, default=0)
    notes = models.TextField(blank=True)

    # 'betalingskenmerk', parsed from notes. Minimum of 7 digits, max of 16
    payment_reference = models.TextField(max_length=20, blank=True)

    def __repr__(self):
        return f'Transaction({self.pk!r}, {self.account!r}, {self.amount!r}, {self.description!r})'

    def __str__(self):
        return f'{self.account}, {self.amount}, {self.description}'

    @property
    def real_amount(self):
        """Ensures the amount of money is always positive, as a withdrawal itself also is a positive number

        :return: positive amount of money
        :rtype: float
        """
        if self.withdrawal:
            return -1 * self.amount
        return self.amount


class PaymentParty(BaseModel):
    """A vendor, person or whatever (think supermarket, pizzeria, bank)"""
    title = models.CharField(max_length=255)
    #hash?
    #lebenstein distance thingee?
    #regexp?
    category = models.IntegerField(choices=PAYMENTPARTY_CATEGORIES, default=PAYMENTPARTY_CATEGORIES[0])
    #tags = 


class PaymentPartyInstance(BaseModel):
    """An instance of a PaymentParty, like a specific subsidiary ('filiaal' or something)"""
    paymentparty = models.ForeignKey(PaymentParty, related_name='instances', on_delete=models.CASCADE)

    # IBAN account number
    account = models.CharField(max_length=40)
