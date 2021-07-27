from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import HABForm
from .models import HABModel

from users.models import SiteUser

from django.template.loader import render_to_string
from django.http import JsonResponse


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


@login_required(login_url='/accounts/login/')
def LohitView(request):
    ctx = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        HABforms = HABModel.objects.filter(roll_number__icontains=url_parameter)

    else:
        HABforms = HABModel.objects.all()

    ctx["HABforms"] = HABforms

    if request.is_ajax():
        html = render_to_string(
            template_name="hab_portal/partial/partial_lohit.html", 
            context={"HABforms": HABforms}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'hab_portal/lohit.html', context=ctx)


@login_required(login_url='/accounts/login/')
def BrahmaView(request):
    ctx = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        HABforms = HABModel.objects.filter(roll_number__icontains=url_parameter)

    else:
        HABforms = HABModel.objects.all()

    ctx["HABforms"] = HABforms

    if request.is_ajax():
        html = render_to_string(
            template_name="hab_portal/partial/partial_brahmaputra.html", 
            context={"HABforms": HABforms}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'hab_portal/brahmaputra.html', context=ctx)

@login_required(login_url='/accounts/login/')
def SiangView(request):
    ctx = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        HABforms = HABModel.objects.filter(roll_number__icontains=url_parameter)

    else:
        HABforms = HABModel.objects.all()

    ctx["HABforms"] = HABforms

    if request.is_ajax():
        html = render_to_string(
            template_name="hab_portal/partial/partial_siang.html", 
            context={"HABforms": HABforms}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'hab_portal/siang.html', context=ctx)


@login_required(login_url='/accounts/login/')
def ManasView(request):
    ctx = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        HABforms = HABModel.objects.filter(roll_number__icontains=url_parameter)

    else:
        HABforms = HABModel.objects.all()

    ctx["HABforms"] = HABforms

    if request.is_ajax():
        html = render_to_string(
            template_name="hab_portal/partial/partial_manas.html", 
            context={"HABforms": HABforms}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'hab_portal/manas.html', context=ctx)


@login_required(login_url='/accounts/login/')
def DisangView(request):
    ctx = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        HABforms = HABModel.objects.filter(roll_number__icontains=url_parameter)

    else:
        HABforms = HABModel.objects.all()

    ctx["HABforms"] = HABforms

    if request.is_ajax():
        html = render_to_string(
            template_name="hab_portal/partial/partial_disang.html",
            context={"HABforms": HABforms}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'hab_portal/disang.html', context=ctx)


@login_required(login_url='/accounts/login/')
def KamengView(request):
    ctx = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        HABforms = HABModel.objects.filter(roll_number__icontains=url_parameter)

    else:
        HABforms = HABModel.objects.all()

    ctx["HABforms"] = HABforms

    if request.is_ajax():
        html = render_to_string(
            template_name="hab_portal/partial/partial_kameng.html",
            context={"HABforms": HABforms}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'hab_portal/kameng.html', context=ctx)


@login_required(login_url='/accounts/login/')
def UmiamView(request):
    ctx = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        HABforms = HABModel.objects.filter(roll_number__icontains=url_parameter)

    else:
        HABforms = HABModel.objects.all()

    ctx["HABforms"] = HABforms

    if request.is_ajax():
        html = render_to_string(
            template_name="hab_portal/partial/partial_umiam.html", 
            context={"HABforms": HABforms}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'hab_portal/umiam.html', context=ctx)


@login_required(login_url='/accounts/login/')
def BarakView(request):

    ctx = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        HABforms = HABModel.objects.filter(roll_number__icontains=url_parameter)

    else:
        HABforms = HABModel.objects.all()

    ctx["HABforms"] = HABforms

    if request.is_ajax():
        html = render_to_string(
            template_name="hab_portal/partial/partial_barak.html", 
            context={"HABforms": HABforms}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'hab_portal/barak.html', context=ctx)


@login_required(login_url='/accounts/login/')
def KapiliView(request):
    ctx = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        HABforms = HABModel.objects.filter(roll_number__icontains=url_parameter)

    else:
        HABforms = HABModel.objects.all()

    ctx["HABforms"] = HABforms

    if request.is_ajax():
        html = render_to_string(
            template_name="hab_portal/partial/partial_kapili.html",
            context={"HABforms": HABforms}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'hab_portal/kapili.html', context=ctx)


@login_required(login_url='/accounts/login/')
def DihingView(request):
    ctx = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        HABforms = HABModel.objects.filter(roll_number__icontains=url_parameter)

    else:
        HABforms = HABModel.objects.all()

    ctx["HABforms"] = HABforms

    if request.is_ajax():
        html = render_to_string(
            template_name="hab_portal/partial/partial_dihing.html",
            context={"HABforms": HABforms}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'hab_portal/dihing.html', context=ctx)


@login_required(login_url='/accounts/login/')
def SubanView(request):
    ctx = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        HABforms = HABModel.objects.filter(roll_number__icontains=url_parameter)

    else:
        HABforms = HABModel.objects.all()

    ctx["HABforms"] = HABforms

    if request.is_ajax():
        html = render_to_string(
            template_name="hab_portal/partial/partial_subansiri.html",
            context={"HABforms": HABforms}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'hab_portal/subansiri.html', context=ctx)


@login_required(login_url='/accounts/login/')
def DhanView(request):
    ctx = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        HABforms = HABModel.objects.filter(roll_number__icontains=url_parameter)

    else:
        HABforms = HABModel.objects.all()

    ctx["HABforms"] = HABforms

    if request.is_ajax():
        html = render_to_string(
            template_name="hab_portal/partial/partial_dhansiri.html", 
            context={"HABforms": HABforms}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'hab_portal/dhansiri.html', context=ctx)


@login_required(login_url='/accounts/login/')
def MSHView(request):
    ctx = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        HABforms = HABModel.objects.filter(roll_number__icontains=url_parameter)

    else:
        HABforms = HABModel.objects.all()

    ctx["HABforms"] = HABforms

    if request.is_ajax():
        html = render_to_string(
            template_name="hab_portal/partial/partial_msh.html", 
            context={"HABforms": HABforms}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'hab_portal/msh.html', context=ctx)