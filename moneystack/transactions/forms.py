from django import forms
from .models import MutationsUpload


class MutationsUploadForm(forms.ModelForm):
    class Meta:
        model = MutationsUpload
        fields = ('description', 'document', )


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
