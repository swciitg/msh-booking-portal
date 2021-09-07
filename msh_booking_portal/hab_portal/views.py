from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from .forms import HABForm1,HABdose2, HABdose1

from .models import HABModel, HAB_FIELDS

from users.models import SiteUser
from users.utils import load_from_user_data, save_to_user_data
from .models import HABModel
from users.models import SiteUser
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.views.generic import DetailView


@login_required(login_url='/accounts/login/')
def index(request):
    print(request.user.id)
    user, created = SiteUser.objects.get_or_create(user_id=request.user.id)
    return render(request, 'forms/hab-landing.html', {})


@login_required(login_url='/accounts/login/')
def HABCreate(request):
    if request.method == 'POST':
        try:
            form_instance = HABModel.objects.get(user__user__pk=request.user.id)
            form = HABForm1(request.POST, request.FILES, instance=form_instance)
        except:
            form = HABForm1(request.POST, request.FILES)


        if form.is_valid():
            application = form.save(commit=False)
            application.user = SiteUser.objects.get(user_id=request.user.id)
            application.save()

            save_to_user_data(application.user, request.POST, HAB_FIELDS)

            if application.vaccination_status=='Double Dose':
                return redirect('hab_portal:hab_2')
            else:
                return redirect('hab_portal:hab_1')

    else:
        try:
            form_instance = HABModel.objects.get(user__user__pk=request.user.id)
            form = load_from_user_data(SiteUser.objects.get(user_id=request.user.id), HABForm1(instance=form_instance), HAB_FIELDS)
        except:
            form = load_from_user_data(SiteUser.objects.get(user_id=request.user.id), HABForm1(), HAB_FIELDS)

    return render(request,
                  'forms/hab.html',
                  {'form': form, 'url': 'add'})


@login_required(login_url='/accounts/login/')
def HAB1(request):

    form_instance = HABModel.objects.get(user__user__pk=request.user.id)
    if request.method == 'POST':
        form = HABdose1(request.POST, request.FILES, instance=form_instance)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = SiteUser.objects.get(user__pk=request.user.id)
            application.proof_of_invitation = request.FILES['proof_of_invitation']

            application.save()
            #save_to_user_data(application.user, request.POST, HAB_FIELDS)
            if application.recieved_an_invite=='Yes':
                return redirect('hab_portal:hab_2')
            else:
                return redirect('hab_portal:hab_dose1wait')


    else:
        form = HABdose1(instance=form_instance)

    return render(request,
                  'forms/hab1.html',
                  {'form': form, 'url': 'form1'})



@login_required(login_url='/accounts/login/')
def HAB2(request):

    form_instance = HABModel.objects.get(user__user__pk=request.user.id)
    if request.method == 'POST':
        form = HABdose2(request.POST, request.FILES, instance=form_instance)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = SiteUser.objects.get(user__pk=request.user.id)
            print(request.FILES)
            application.fee_receipt = request.FILES.get('fee_receipt',None)
            application.vaccination_cert = request.FILES.get('vaccination_cert',None)
            application.travel_ticket = request.FILES.get('travel_ticket',None)
            application.rtpcr_report = request.FILES.get('rtpcr_report',None)

            application.save()
            #save_to_user_data(application.user, request.POST, HAB_FIELDS)
            return redirect('hab_portal:hab_thanks')

    else:
        form = HABdose2(instance=form_instance)

    return render(request,
                  'forms/hab2.html',
                  {'form': form, 'url': 'form2'})



@login_required(login_url='/accounts/login/')
def HABDose1Wait(request):
    return render(request,'forms/habdose1wait.html')

@login_required(login_url='/accounts/login/')
def HABEdit(request):
    form_instance = HABModel.objects.get(user__user__pk=request.user.id)
    if request.method == 'POST':
        form = HABForm1(request.POST, request.FILES, instance=form_instance)

        if form.is_valid() and (not form_instance.locked):
            application = form.save(commit=False)
            application.user = SiteUser.objects.get(user__pk=request.user.id)
            application.fee_receipt = request.FILES['fee_receipt']
            application.save()
            save_to_user_data(application.user, request.POST, HAB_FIELDS)
            return redirect('hab_portal:hab_thanks')

    else:
        form = HABForm1(instance=form_instance)

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
# @permission_required('hab_portal.can_view_brahma_hostel_data')
def HostelRejected(request,hostel):
    ctx = {'Hostel': hostel}
    url_parameter = request.GET.get("q")

    if url_parameter:
        HABforms = HABModel.objects.filter(roll_number__icontains=url_parameter)

    else:
        HABforms = HABModel.objects.all()
    ctx["HABforms"] = HABforms
    if request.is_ajax():
        html = render_to_string(
            template_name="hab_portal/partial/partial_rejected.html", 
            context={"HABforms": HABforms, 'Hostel': hostel}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'hab_portal/complete/rejected.html', context=ctx)


@login_required(login_url='/accounts/login/')
# @permission_required('hab_portal.can_view_brahma_hostel_data')
def HostelStatusAccept(request, hostel, status, id):
    application = HABModel.objects.get(pk=id)
    application.status = 'Accepted'
    application.save()
    return redirect("hab_portal:hostel-view", hostel=hostel)


@login_required(login_url='/accounts/login/')
# @permission_required('hab_portal.can_view_brahma_hostel_data')
def HostelStatusDecline(request, hostel, id):
    application = HABModel.objects.get(pk=id)
    application.status = 'Declined'
    application.save()
    return redirect("hab_portal:hostel-view", hostel=hostel)
