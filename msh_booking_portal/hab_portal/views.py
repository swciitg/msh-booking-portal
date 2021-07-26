from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import HABForm
from .models import HABModel

from users.models import SiteUser
from django.views import generic

#class HABList(generic.ListView):
#    queryset = HABModel.objects.filter(status=1).order_by('-date_of_arrival')
#    template_name = 'hab_portal/hab-view.html'

#class StudentDetail(generic.DetailView):
#    model = HABModel
#    template_name = 'student_detail.html'


@login_required(login_url='/accounts/login/')
def index(request):
    user, created = SiteUser.objects.get_or_create(user_id=request.user.id)
    return render(request, 'index.html', {})


def HABCreate(request):
    if request.method == 'POST':
        form = HABForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = SiteUser.objects.get(user__pk=request.user.id)
            application.save()
            return redirect('../thanks/')

    else:
        form = HABForm()

    return render(request,
                  'forms/hab.html',
                  {'form': form, 'url': 'add'})


def HABEdit(request):
    form_instance = HABModel.objects.get(user__user__pk=request.user.id)
    if request.method == 'POST':
        form = HABForm(request.POST, instance=form_instance)

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


def HABThanks(request):
    return render(request,
                  'forms/hab-thanks.html')


def HABView(request):
    return render(request,
                  'hab_portal/hab-view.html',
                  {'applications': HABModel.objects.all(),
                   'hostels': HABModel.hostel, })

def LohitView(request):
    return render(request,
                  'hab_portal/lohit.html',
                  {'applications': HABModel.objects.all(),
                   'hostels': HABModel.hostel, })

def BrahmaView(request):
    return render(request,
                  'hab_portal/brahmaputra.html',
                  {'applications': HABModel.objects.all(),
                   'hostels': HABModel.hostel, })

def SiangView(request):
    return render(request,
                  'hab_portal/siang.html',
                  {'applications': HABModel.objects.all(),
                   'hostels': HABModel.hostel, })

def ManasView(request):
    return render(request,
                  'hab_portal/manas.html',
                  {'applications': HABModel.objects.all(),
                   'hostels': HABModel.hostel, })

def DisangView(request):
    return render(request,
                  'hab_portal/disang.html',
                  {'applications': HABModel.objects.all(),
                   'hostels': HABModel.hostel, })

def KamengView(request):
    return render(request,
                  'hab_portal/kameng.html',
                  {'applications': HABModel.objects.all(),
                   'hostels': HABModel.hostel, })

def UmiamView(request):
    return render(request,
                  'hab_portal/umiam.html',
                  {'applications': HABModel.objects.all(),
                   'hostels': HABModel.hostel, })

def BarakView(request):
    return render(request,
                  'hab_portal/barak.html',
                  {'applications': HABModel.objects.all(),
                   'hostels': HABModel.hostel, })

def KapiliView(request):
    return render(request,
                  'hab_portal/kapili.html',
                  {'applications': HABModel.objects.all(),
                   'hostels': HABModel.hostel, })

def DihingView(request):
    return render(request,
                  'hab_portal/dihing.html',
                  {'applications': HABModel.objects.all(),
                   'hostels': HABModel.hostel, })

def SubanView(request):
    return render(request,
                  'hab_portal/subansiri.html',
                  {'applications': HABModel.objects.all(),
                   'hostels': HABModel.hostel, })

def DhanView(request):
    return render(request,
                  'hab_portal/dhansiri.html',
                  {'applications': HABModel.objects.all(),
                   'hostels': HABModel.hostel, })

def MSHView(request):
    return render(request,
                  'hab_portal/msh.html',
                  {'applications': HABModel.objects.all(),
                   'hostels': HABModel.hostel, })