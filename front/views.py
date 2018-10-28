from django.shortcuts import render, redirect
from . import forms

def index(request):
    form = forms.MDForm()
    return render(request, 'front/index.html', {'form': form})

def store(request):
    print(request.POST.get('mdfield', ''))
    return redirect('/front')
