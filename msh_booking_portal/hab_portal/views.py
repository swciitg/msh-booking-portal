from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

from .forms import HABForm
from .models import HABModel

from users.models import SiteUser


@login_required(login_url='/accounts/login/')
def index(request):
    user, created = SiteUser.objects.get_or_create(user_id=request.user.id)
    return render(request, 'index.html', {})


@login_required(login_url='/accounts/login/')
def HABCreate(request):
    if request.method == 'POST':
        form = HABForm(request.POST, request.FILES)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = SiteUser.objects.get(user__pk=request.user.id)
            application.fee_receipt = request.FILES['fee_receipt']
            application.save()
            return redirect('../thanks/')

    else:
        form = HABForm()

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
                  'hab_portal/hab-view.html',
                  {'applications': HABModel.objects.all().order_by('time_of_submission'),
                   'hostels': HABModel.hostel })


@login_required(login_url='/accounts/login/')
def HABDetail(request, slug):
    HABform = HABModel.objects.get(slug=slug)
    return render(request, 'hab_portal/hab-detail.html', { 'HABform': HABform })                   

@permission_required('hab_portal.can_view_lohit_hostel_data')
def LohitView(request):
    return render(request,
                  'hab_portal/lohit.html',
                  {'applications': HABModel.objects.all(),
                   'hostels': HABModel.hostel, })

@permission_required('hab_portal.can_view_brahma_hostel_data')
def BrahmaView(request):
    return render(request,
                  'hab_portal/brahmaputra.html',
                  {'applications': HABModel.objects.all(),
                   'hostels': HABModel.hostel, })

@permission_required('hab_portal.can_view_siang_hostel_data')
def SiangView(request):
    return render(request,
                  'hab_portal/siang.html',
                  {'applications': HABModel.objects.all(),
                   'hostels': HABModel.hostel, })

@permission_required('hab_portal.can_view_manas_hostel_data')
def ManasView(request):
    return render(request,
                  'hab_portal/manas.html',
                  {'applications': HABModel.objects.all(),
                   'hostels': HABModel.hostel, })

@permission_required('hab_portal.can_view_disang_hostel_data')
def DisangView(request):
    return render(request,
                  'hab_portal/disang.html',
                  {'applications': HABModel.objects.all(),
                   'hostels': HABModel.hostel, })

@permission_required('hab_portal.can_view_kameng_hostel_data')
def KamengView(request):
    return render(request,
                  'hab_portal/kameng.html',
                  {'applications': HABModel.objects.all(),
                   'hostels': HABModel.hostel, })

@permission_required('hab_portal.can_view_umiam_hostel_data')
def UmiamView(request):
    return render(request,
                  'hab_portal/umiam.html',
                  {'applications': HABModel.objects.all(),
                   'hostels': HABModel.hostel, })

@permission_required('hab_portal.can_view_barak_hostel_data')
def BarakView(request):
    return render(request,
                  'hab_portal/barak.html',
                  {'applications': HABModel.objects.all(),
                   'hostels': HABModel.hostel, })

@permission_required('hab_portal.can_view_kapili_hostel_data')
def KapiliView(request):
    return render(request,
                  'hab_portal/kapili.html',
                  {'applications': HABModel.objects.all(),
                   'hostels': HABModel.hostel, })

@permission_required('hab_portal.can_view_dihing_hostel_data')
def DihingView(request):
    return render(request,
                  'hab_portal/dihing.html',
                  {'applications': HABModel.objects.all(),
                   'hostels': HABModel.hostel, })

@permission_required('hab_portal.can_view_suban_hostel_data')
def SubanView(request):
    return render(request,
                  'hab_portal/subansiri.html',
                  {'applications': HABModel.objects.all(),
                   'hostels': HABModel.hostel, })

@permission_required('hab_portal.can_view_dhan_hostel_data')
def DhanView(request):
    return render(request,
                  'hab_portal/dhansiri.html',
                  {'applications': HABModel.objects.all(),
                   'hostels': HABModel.hostel, })

@permission_required('hab_portal.can_view_dhan_hostel_data')
def MSHView(request):
    return render(request,
                  'hab_portal/msh.html',
                  {'applications': HABModel.objects.all(),
                   'hostels': HABModel.hostel, })