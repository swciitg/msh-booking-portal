from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import AVAILABLE_FORMS, SampleForm, MSHForm
from .models import SampleModel, MSHModel

from users.models import SiteUser

@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'index.html', {})

def MSHCreate(request):
    if request.method == 'POST':
        form = MSHForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = SiteUser.objects.get(pk=request.user.id)
            application.save()
            return redirect('../thanks/')

    elif request.method == 'GET':
        form = MSHForm()

    return render(request,
                  'forms/msh.html',
                  {'form': form, 'url':'add'})

def MSHEdit(request):
    form_instance = MSHModel.objects.get(user__user__pk=request.user.id)
    if request.method == 'POST':
        form = MSHForm(request.POST, instance=form_instance)

        if form.is_valid() and (form_instance.locked == False):
            form.save()
            return redirect('../thanks/')

    elif request.method == 'GET':
        form = MSHForm(instance=form_instance)

        if form_instance.locked:
            for field in form.fields:
                form.fields[field].disabled = True

    return render(request,
                  'forms/msh.html',
                  {'form': form, 'url':'edit', 'locked': form_instance.locked})

def MSHThanks(request):
    return render(request,
                  'forms/msh-thanks.html')