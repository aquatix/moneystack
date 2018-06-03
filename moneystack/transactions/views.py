from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import MutationsUploadForm


def index(request):
    return render(request, 'overview.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = MutationsUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MutationsUploadForm()
    return render(request, 'upload.html', {
        'form': form
    })
