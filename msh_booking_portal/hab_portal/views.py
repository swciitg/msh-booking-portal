from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from .forms import HABForm
from .models import HABModel
from users.models import SiteUser
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.views.generic import DetailView



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
            return redirect("hab_portal:hab_thanks")

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
            return redirect("hab_portal:hab_thanks")

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


# @login_required(login_url='/accounts/login/')
class HABDetailView(DetailView):
    model=HABModel                 


@login_required(login_url='/accounts/login/')
# @permission_required('hab_portal.can_view_siang_hostel_data')
def HostelView(request,hostel):
    ctx = {'Hostel':hostel}
    url_parameter = request.GET.get("q")

    if url_parameter:
        HABforms = HABModel.objects.filter(roll_number__icontains=url_parameter)

    else:
        HABforms = HABModel.objects.all()

    ctx["HABforms"] = HABforms

    if request.is_ajax():
        html = render_to_string(
            template_name="hab_portal/partial/partial_hostels.html", 
            context={"HABforms": HABforms, 'Hostel':hostel}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'hab_portal/complete/hostels.html', context=ctx)


@login_required(login_url='/accounts/login/')
# @permission_required('hab_portal.can_view_brahma_hostel_data')
def HostelApproved(request, hostel):
    ctx = {'Hostel':hostel}
    url_parameter = request.GET.get("q")

    if url_parameter:
        HABforms = HABModel.objects.filter(roll_number__icontains=url_parameter)

    else:
        HABforms = HABModel.objects.all()

    ctx["HABforms"] = HABforms

    if request.is_ajax():
        html = render_to_string(
            template_name="hab_portal/partial/partial_approved.html", 
            context={"HABforms": HABforms,'Hostel':hostel}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'hab_portal/complete/approved.html', context=ctx)


@login_required(login_url='/accounts/login/')
# @permission_required('hab_portal.can_view_brahma_hostel_data')
def HostelPending(request,hostel):
    ctx = {'Hostel':hostel}
    url_parameter = request.GET.get("q")

    if url_parameter:
        HABforms = HABModel.objects.filter(roll_number__icontains=url_parameter)

    else:
        HABforms = HABModel.objects.all()

    ctx["HABforms"] = HABforms

    if request.is_ajax():
        html = render_to_string(
            template_name="hab_portal/partial/partial_pending.html", 
            context={"HABforms": HABforms, 'Hostel':hostel}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'hab_portal/complete/pending.html', context=ctx)


@login_required(login_url='/accounts/login/')
@permission_required('hab_portal.can_view_brahma_hostel_data')
def HostelRejected(request,hostel):
    ctx = {'Hostel':hostel}
    url_parameter = request.GET.get("q")

    if url_parameter:
        HABforms = HABModel.objects.filter(roll_number__icontains=url_parameter)

    else:
        HABforms = HABModel.objects.all()
    ctx["HABforms"] = HABforms
    if request.is_ajax():
        html = render_to_string(
            template_name="hab_portal/partial/partial_rejected.html", 
            context={"HABforms": HABforms, 'Hostel':hostel}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'hab_portal/complete/rejected.html', context=ctx)


@login_required(login_url='/accounts/login/')
# @permission_required('hab_portal.can_view_brahma_hostel_data')
def HostelStatusAccept(request,hostel,status,id):
    application = HABModel.objects.get(pk=id)
    application.status = 'Accepted'
    application.save()
    return redirect("hab_portal:hostel-view", hostel=hostel)


@login_required(login_url='/accounts/login/')
# @permission_required('hab_portal.can_view_brahma_hostel_data')
def HostelStatusDecline(request,hostel,id):
    application = HABModel.objects.get(pk=id)
    application.status = 'Declined'
    application.save()
    return redirect("hab_portal:hostel-view", hostel=hostel)