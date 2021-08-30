from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import HABForm
from .models import HABModel, HAB_FIELDS

from users.models import SiteUser
from users.utils import load_from_user_data, save_to_user_data


@login_required(login_url='/accounts/login/')
def index(request):
    user, created = SiteUser.objects.get_or_create(user_id=request.user.id)
    return render(request, 'forms/hab-landing.html', {})


@login_required(login_url='/accounts/login/')
def HABCreate(request):
    if request.method == 'POST':
        form = HABForm(request.POST, request.FILES)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = SiteUser.objects.get(user__pk=request.user.id)
            application.fee_receipt = request.FILES['fee_receipt']
            application.save()
            save_to_user_data(application.user, request.POST, HAB_FIELDS)
            return redirect('../thanks/')

    else:
        form = load_from_user_data(SiteUser.objects.get(user__pk=request.user.id), HABForm(), HAB_FIELDS)

    return render(request,
                  'forms/hab.html',
                  {'form': form, 'url': 'add'})


@login_required(login_url='/accounts/login/')
def HABEdit(request):
    form_instance = HABModel.objects.get(user__user__pk=request.user.id)
    if request.method == 'POST':
        form = HABForm(request.POST, request.FILES, instance=form_instance)

        if form.is_valid() and (not form_instance.locked):
            form.save()
            save_to_user_data(form.user, request.POST, HAB_FIELDS)
            return redirect('../thanks/')

    else:
        form = HABForm(instance=form_instance)

        if form_instance.locked:
            for field in form.fields:
                form.fields[field].disabled = True

    return render(request,
                  'forms/hab.html',
                  {'form': form, 'url': 'edit', 'locked': form_instance.locked})


@login_required(login_url='/accounts/login/')
def HABThanks(request):
    return render(request,
                  'forms/hab-thanks.html')


@login_required(login_url='/accounts/login/')
def HABView(request):
    return render(request,
                  'forms/hab-view.html',
                  {'applications': HABModel.objects.all(), })
