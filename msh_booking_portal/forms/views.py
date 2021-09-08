from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import AVAILABLE_FORMS, SampleForm, MSHForm
from .models import SampleModel, MSHModel

from users.models import SiteUser


@login_required(login_url='/campus_return/accounts/login/')
def index(request):
    user, created = SiteUser.objects.get_or_create(user_id=request.user.id)
    return render(request, 'index.html', {})


@login_required(login_url='/campus_return/accounts/login/')
def MSHCreate(request):
    if request.method == 'POST':
        form = MSHForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = SiteUser.objects.get(user__pk=request.user.id)
            application.save()
            return redirect('../thanks/')

    else:
        form = MSHForm()

    return render(request,
                  'forms/msh.html',
                  {'form': form, 'url': 'add'})


@login_required(login_url='/campus_return/accounts/login/')
def MSHEdit(request):
    form_instance = MSHModel.objects.get(user__user__pk=request.user.id)
    if request.method == 'POST':
        form = MSHForm(request.POST, instance=form_instance)

        if form.is_valid() and (not form_instance.locked):
            form.save()
            return redirect('../thanks/')

    else:
        form = MSHForm(instance=form_instance)

        if form_instance.locked:
            for field in form.fields:
                form.fields[field].disabled = True

    return render(request,
                  'forms/msh.html',
                  {'form': form, 'url': 'edit', 'locked': form_instance.locked})


@login_required(login_url='/campus_return/accounts/login/')
def MSHThanks(request):
    return render(request,
                  'forms/msh-thanks.html')


@login_required(login_url='/campus_return/accounts/login/')
def MSHView(request):
    return render(request,
                  'forms/msh-view.html',
                  {'applications': MSHModel.objects.all(),})