from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import AVAILABLE_FORMS, SampleForm
from .models import SampleModel

@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'index.html', {})

def MSHCreate(request):
    if request.method == 'POST':
        form = SampleForm(request.POST, user=request.user)

        if form.is_valid():
            form.save()
            return redirect('../thanks/')

    elif request.method == 'GET':
        form = SampleForm()

    return render(request,
                  'forms/msh.html',
                  {'form': form})

def MSHThanks(request):
    return render(request,
                  'forms/msh-thanks.html')