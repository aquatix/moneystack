from django.utils.translation import gettext as _


MUTATION_FILE_TYPES = (
    (1, _('ING Bank')),
    (2, _('ABN Amro Bank')),
)

PAYMENTPARTY_CATEGORIES = (
    (0, _('Ongecategoriseerd')),
    (1, _('Onbekend')),
    (2, _('Boodschappen')),
    (3, _('Horeca')),
    (4, _('Electronica')),
)
