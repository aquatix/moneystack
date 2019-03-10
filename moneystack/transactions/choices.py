from django.utils.translation import gettext as _


MUTATION_FILE_TYPES = (
    (1, _('ING Bank')),
    (2, _('ABN Amro Bank')),
)

MUTATION_TYPES = (
    (0, _('Unknown')),
    (1, _('Acceptgiro')),
    (2, _('Betaalautomaat')),
    (3, _('Diversen')),
    (4, _('Filiaal overschrijving')),
    (5, _('Saldolijn')),
    (6, _('Geldautomaat')),
    (7, _('Internetbankieren')),
    (8, _('Incasso')),
    (9, _('Overschrijving')),
    (10, _('Opname kantoor')),
    (11, _('Periodieke overschrijving')),
    (12, _('Storting')),
    (13, _('Verzamelbetaling')),
)

PAYMENTPARTY_CATEGORIES = (
    (0, _('Ongecategoriseerd')),
    (1, _('Onbekend')),
    (2, _('Boodschappen')),
    (3, _('Horeca')),
    (4, _('Electronica')),
)
