from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from .forms import HABForm1, HABdose2, HABdose1, PdfgeneratedForm

from .models import HABModel, HAB_FIELDS

from users.models import SiteUser
from users.utils import load_from_user_data, save_to_user_data
from .models import HABModel
from django.template.loader import render_to_string
from django.http import JsonResponse, FileResponse
from django.views.generic import DetailView
from django.core.exceptions import ObjectDoesNotExist

from io import BytesIO
from django.http import HttpResponse, HttpResponseForbidden
from django.template.loader import get_template

from xhtml2pdf import pisa

from django.core.files import File
from PyPDF2 import PdfFileMerger, PdfFileReader

import xlwt
from django.http import HttpResponse
import datetime


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def generate_obj_pdf(instance_id):
    obj = HABModel.objects.get(id=instance_id)
    # form = PdfgeneratedForm(instance=obj)
    context = {'form': obj}
    # print(form)
    pdf = render_to_pdf('pdf_gen.html', context)
    obj.final_pdf.save('final_pdf'+str(instance_id),
                       File(BytesIO(pdf.content)))


@login_required(login_url='/campus_return/accounts/login/')
def index(request):
    user, created = SiteUser.objects.get_or_create(user_id=request.user.id)
    return render(request, 'forms/hab-landing.html', {})


@login_required(login_url='/campus_return/accounts/login/')
def HABCreate(request):
    if request.method == 'POST':
        try:
            form_instance = HABModel.objects.get(
                user__user__pk=request.user.id)
            form = HABForm1(request.POST, request.FILES,
                            instance=form_instance)
        except:
            form = HABForm1(request.POST, request.FILES)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = SiteUser.objects.get(user_id=request.user.id)
            application.save()

            save_to_user_data(application.user, request.POST, HAB_FIELDS)

            if (application.vaccination_status == 'Single Dose') or (application.returning_from_state == 'Kerala'):
                return redirect('hab_portal:hab_1')
            else:
                return redirect('hab_portal:hab_2')

    else:
        try:
            form_instance = HABModel.objects.get(
                user__user__pk=request.user.id)
            form = load_from_user_data(SiteUser.objects.get(
                user_id=request.user.id), HABForm1(instance=form_instance), HAB_FIELDS)
        except:
            form = load_from_user_data(SiteUser.objects.get(
                user_id=request.user.id), HABForm1(), HAB_FIELDS)

    return render(request,
                  'forms/hab.html',
                  {'form': form, 'url': 'add'})


@login_required(login_url='/campus_return/accounts/login/')
def HAB1(request):
    try:
        form_instance = HABModel.objects.get(user__user__pk=request.user.id)
        if request.method == 'POST':
            form = HABdose1(request.POST, request.FILES,
                            instance=form_instance)

            if form.is_valid():
                application = form.save(commit=False)
                application.user = SiteUser.objects.get(
                    user__pk=request.user.id)
                if request.FILES.get('proof_of_invitation'):
                    application.proof_of_invitation = request.FILES.get(
                        'proof_of_invitation')

                application.save()
                #save_to_user_data(application.user, request.POST, HAB_FIELDS)
                if application.recieved_an_invite == 'Yes':
                    return redirect('hab_portal:hab_2')
                else:
                    return redirect('hab_portal:hab_dose1wait')

        else:
            form = HABdose1(instance=form_instance)

        return render(request,
                      'forms/hab1.html',
                      {'form': form, 'url': 'form1'})
    except ObjectDoesNotExist:
        return redirect('hab_portal:hab_create')


@login_required(login_url='/campus_return/accounts/login/')
def HAB2(request):
    try:
        form_instance = HABModel.objects.get(user__user__pk=request.user.id)
        request.session['id'] = form_instance.id
        if request.method == 'POST':
            form = HABdose2(request.POST, request.FILES,
                            instance=form_instance)

            if form.is_valid():
                application = form.save(commit=False)
                application.user = SiteUser.objects.get(
                    user__pk=request.user.id)
                if request.FILES.get('fee_receipt', None):
                    application.fee_receipt = request.FILES.get(
                        'fee_receipt', None)
                if request.FILES.get('vaccination_cert', None):
                    application.vaccination_cert = request.FILES.get(
                        'vaccination_cert', None)
                if request.FILES.get('travel_ticket', None):
                    application.travel_ticket = request.FILES.get(
                        'travel_ticket', None)
                if request.FILES.get('rtpcr_report', None):
                    application.rtpcr_report = request.FILES.get(
                        'rtpcr_report', None)
                application.save()
                generate_obj_pdf(form_instance.id)
                #save_to_user_data(application.user, request.POST, HAB_FIELDS)
                return redirect('hab_portal:hab_thanks')

        else:
            form = HABdose2(instance=form_instance)

        return render(request,
                      'forms/hab2.html',
                      {'form': form, 'url': 'form2'})

    except ObjectDoesNotExist:
        return redirect('hab_portal:hab_create')


@login_required(login_url='/campus_return/accounts/login/')
def HABDose1Wait(request):
    return render(request, 'forms/habdose1wait.html')


@login_required(login_url='/campus_return/accounts/login/')
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


@login_required(login_url='/campus_return/accounts/login/')
def HABThanks(request):
    instance_id = request.session.get('id')
    obj = HABModel.objects.get(id=instance_id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; inline; filename="somefilename.pdf"'
    buffer = BytesIO()
    pdf1_buffer = obj.final_pdf
    pdf2_buffer = obj.vaccination_cert

    pdf_merger = PdfFileMerger(strict=False)
    pdf_merger.append(pdf1_buffer)
    pdf_merger.append(obj.fee_receipt)
    pdf_merger.append(pdf2_buffer)
    pdf_merger.append(obj.travel_ticket)
    pdf_merger.append(obj.rtpcr_report)
    if obj.vaccination_status == "Single Dose":
        pdf_merger.append(obj.proof_of_invitation)

    # This can probably be improved
    pdf_merger.write(buffer)
    pdf_merger.close()
    buffer.seek(0)

    response.write(buffer.getvalue())

    obj.final_pdf.save('final_pdf'+str(instance_id),
                       File(BytesIO(response.content)))
    return render(request,
                  'forms/hab-thanks.html',{'file':obj})


@login_required(login_url='/campus_return/accounts/login/')
def AdminView(request):
    if request.user.is_staff:
        url_parameter = request.GET.get("q")

        if url_parameter:
            HABforms = HABModel.objects.filter(
                roll_number__icontains=url_parameter)

        else:
            HABforms = HABModel.objects.all()

        if request.is_ajax():
            html = render_to_string(
                template_name="hab_portal/partial/partial_invite.html",
                context={"HABforms": HABforms}
            )

            data_dict = {"html_from_view": html}

            return JsonResponse(data=data_dict, safe=False)
        context = {"HABforms": HABforms}
        return render(request, 'hab_portal/complete/invite.html', context)
    else:
        return HttpResponseForbidden()

def MarkAsInvited(request, id=-1):
    if request.user.is_staff:
        if (id == -1):
            return JsonResponse({'success': False})
        model = HABModel.objects.get(pk=id)
        model.invite_sent = 'Invited'
        model.save()
        return JsonResponse(data={'success': True})
    else:
        return HttpResponseForbidden()


def MarkAsNotInvited(request, id=-1):
    if request.user.is_staff:
        if (id == -1):
            return JsonResponse({'success': False})
        model = HABModel.objects.get(pk=id)
        model.invite_sent = 'Not Invited'
        model.save()
        return JsonResponse(data={'success': True})
    else:
        return HttpResponseForbidden()


@login_required(login_url='/campus_return/accounts/login/')
def HABView(request):
    return render(request,
                  'hab_portal/hab-view.html',
                  {'applications': HABModel.objects.all().order_by('time_of_submission'),
                   'hostels': HABModel.hostel})


@login_required(login_url='/campus_return/accounts/login/')
def HostelView(request,hostel):
    if request.user.is_staff:
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
    else:
        return HttpResponseForbidden()


@login_required(login_url='/campus_return/accounts/login/')
def HostelApproved(request, hostel):
    if request.user.is_staff:
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
    else:
        return HttpResponseForbidden()


@login_required(login_url='/campus_return/accounts/login/')
def HostelPending(request,hostel):
    if request.user.is_staff:
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
    else:
        return HttpResponseForbidden()


@login_required(login_url='/campus_return/accounts/login/')
def HostelRejected(request, hostel):
    if request.user.is_staff:
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
    else:
        return HttpResponseForbidden()


@login_required(login_url='/campus_return/accounts/login/')
def HostelStatusAccept(request, hostel, id):
    if request.user.is_staff:
        application = HABModel.objects.get(pk=id)
        application.status = 'Verified'
        application.save()
        return redirect("hab_portal:hostel-view", hostel=hostel)
    else:
        return HttpResponseForbidden()


@login_required(login_url='/campus_return/accounts/login/')
def HostelStatusDecline(request, hostel, id):
    if request.user.is_staff:
        application = HABModel.objects.get(pk=id)
        application.status = 'Not Verified'
        application.save()
        return redirect("hab_portal:hostel-view", hostel=hostel)
    else:
        return HttpResponseForbidden()


@login_required(login_url='/campus_return/accounts/login/')
def MediaView(request, file):
    if request.user.is_staff:
        return FileResponse(open('media/hab_portal/' + file, 'rb'))

    folder = file.split('/')[0]

    try:
        if folder == 'proof_of_invitation':
            instance = HABModel.objects.get(user__user__pk=request.user.id)
            if (instance.proof_of_invitation.name == 'hab_portal/' + file):
                return FileResponse(open('media/hab_portal/' + file, 'rb'))
            else:
                return HttpResponseForbidden()

        if folder == 'fee_recipt':
            instance = HABModel.objects.get(user__user__pk=request.user.id)
            if (instance.fee_receipt.name == 'hab_portal/' + file):
                return FileResponse(open('media/hab_portal/' + file, 'rb'))
            else:
                return HttpResponseForbidden()

        if folder == 'vaccination':
            instance = HABModel.objects.get(user__user__pk=request.user.id)
            if (instance.vaccination_cert.name == 'hab_portal/' + file):
                return FileResponse(open('media/hab_portal/' + file, 'rb'))
            else:
                return HttpResponseForbidden()

        if folder == 'rtpcr':
            instance = HABModel.objects.get(user__user__pk=request.user.id)
            if (instance.rtpcr_report.name == 'hab_portal/' + file):
                return FileResponse(open('media/hab_portal/' + file, 'rb'))
            else:
                return HttpResponseForbidden()

        if folder == 'travel':
            instance = HABModel.objects.get(user__user__pk=request.user.id)
            if (instance.travel_ticket.name == 'hab_portal/' + file) or request.user.is_staff:
                return FileResponse(open('media/hab_portal/' + file, 'rb'))
            else:
                return HttpResponseForbidden()

        if folder == 'final_pdf':
            instance = HABModel.objects.get(user__user__pk=request.user.id)
            if (instance.final_pdf.name == 'hab_portal/' + file) or request.user.is_staff:
                return FileResponse(open('media/hab_portal/' + file, 'rb'))
            else:
                return HttpResponseForbidden()

    except:
        return HttpResponseForbidden()


@login_required(login_url='/campus_return/accounts/login/')
def Download_Excel(request):

    response = HttpResponse(content_type='application/ms-excel')

    response['Content-Disposition'] = 'attachment; filename=Invitation List ' + \
        str(datetime.datetime.now())+'.xls'

    wb = xlwt.Workbook(encoding='utf-8')

    ws = wb.add_sheet("sheet1")

    row_num = 0

    font_style = xlwt.XFStyle()

    font_style.font.bold = True

    columns = ['Name', 'Roll Number', 'Email', 'Programme', 'State']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = HABModel.objects.filter(recieved_an_invite='No').values_list(
        'name', 'roll_number', 'email', 'programme', 'returning_from_state')

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)

    return response
