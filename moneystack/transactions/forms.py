from django import forms
from .models import MutationsUpload


class MutationsUploadForm(forms.ModelForm):
    class Meta:
        model = MutationsUpload
        fields = ('description', 'document', )
