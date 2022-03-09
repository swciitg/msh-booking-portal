from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

from .forms import PdfgeneratedForm
from .models import HABModel, NewHABModel, CampusReturn2022
from .models import HAB_FIELDS
# from .forms import HABForm1, HABdose1, HABdose2
# from .forms import NewHABForm1, NewHABdose1, NewHABForm2
from .forms import CampusReturn2022Form1, CampusReturn2022Form2

from users.models import SiteUser
from users.utils import load_from_user_data, save_to_user_data
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
import pikepdf
import xlwt
from django.http import HttpResponse
import datetime
from pytz import timezone
from django.db.models import Q
from django.contrib import messages
from PyPDF2 import PdfFileReader, utils


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)

    # IST_timezone = timezone('Asia/Kolkata')

    # context_dict['form'].date_of_arrival = context_dict['form'].date_of_arrival
    # context_dict['form'].check_in_date = context_dict['form'].check_in_date.astimezone(IST_timezone)

    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def generate_obj_pdf(instance_id):
    obj = CampusReturn2022.objects.get(id=instance_id)
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
    user, created = SiteUser.objects.get_or_create(user_id=request.user.id)
    if request.method == 'POST':
        try:
            form_instance = CampusReturn2022.objects.get(user__user__pk=request.user.id)
            form = CampusReturn2022Form1(request.POST, request.FILES, instance=form_instance)

        except:
            form = CampusReturn2022Form1(request.POST, request.FILES)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = SiteUser.objects.get(user_id=request.user.id)
            application.email = user.user.email

            if request.FILES.get('vaccination_cert', None):
                application.vaccination_cert = request.FILES.get(
                    'vaccination_cert', None)
                try:
                    PdfFileReader(application.vaccination_cert)
                except utils.PdfReadError:
                    messages.error(request, 'Unsupported Format or Corrupt PDF for Vaccination Certificate')
                    return redirect('hab_portal:hab')

            application.save()

            save_to_user_data(application.user, request.POST, HAB_FIELDS)

            # if (application.vaccination_status == 'Single Dose'):
            #     return redirect('hab_portal:hab_1')
            # else:
            #     return redirect('hab_portal:hab_2')

            return redirect('hab_portal:hab_2')

    else:
        try:
            form_instance = CampusReturn2022.objects.get(user__user__pk=request.user.id)
            form = load_from_user_data(SiteUser.objects.get(user_id=request.user.id),
                                       CampusReturn2022Form1(instance=form_instance),
                                       HAB_FIELDS)
        except:
            form = load_from_user_data(SiteUser.objects.get(user_id=request.user.id),
                                       CampusReturn2022Form1(),
                                       HAB_FIELDS)

    return render(request,
                  'forms/hab.html',
                  {'form': form, 'url': 'add'})


# @login_required(login_url='/campus_return/accounts/login/')
# def HAB1(request):
#     try:
#         form_instance = CampusReturn2022.objects.get(user__user__pk=request.user.id)
#         if request.method == 'POST':
#             form = NewHABdose1(request.POST, request.FILES,
#                             instance=form_instance)
#
#             if form.is_valid():
#                 application = form.save(commit=False)
#                 application.user = SiteUser.objects.get(
#                     user__pk=request.user.id)
#                 if request.FILES.get('proof_of_invitation'):
#                     application.proof_of_invitation = request.FILES.get(
#                         'proof_of_invitation')
#
#                 application.save()
#                 #save_to_user_data(application.user, request.POST, HAB_FIELDS)
#                 if application.recieved_an_invite == 'Yes':
#                     return redirect('hab_portal:hab_2')
#                 else:
#                     return redirect('hab_portal:hab_dose1wait')
#
#         else:
#             form = NewHABdose1(instance=form_instance)
#
#         return render(request,
#                       'forms/hab1.html',
#                       {'form': form, 'url': 'form1'})
#     except ObjectDoesNotExist:
#         return redirect('hab_portal:hab_create')


@login_required(login_url='/campus_return/accounts/login/')
def HAB2(request):
    try:
        form_instance = CampusReturn2022.objects.get(user__user__pk=request.user.id)
        request.session['id'] = form_instance.id
        if request.method == 'POST':
            form = CampusReturn2022Form2(request.POST, request.FILES,
                            instance=form_instance)

            if form.is_valid():
                application = form.save(commit=False)
                application.user = SiteUser.objects.get(
                    user__pk=request.user.id)
                if request.FILES.get('fee_receipt', None):
                    application.fee_receipt = request.FILES.get(
                        'fee_receipt', None)
                    try:
                        PdfFileReader(application.fee_receipt)
                    except utils.PdfReadError:
                        messages.error(request, 'Unsupported Format or Corrupt PDF for Fee Receipt')
                        return redirect('hab_portal:hab_2')

                if request.FILES.get('travel_ticket', None):
                    application.travel_ticket = request.FILES.get(
                        'travel_ticket', None)
                    try:
                        PdfFileReader(application.travel_ticket)
                    except utils.PdfReadError:
                        messages.error(request, 'Unsupported Format or Corrupt PDF for Travel Ticket')
                        return redirect('hab_portal:hab_2')

                # if request.FILES.get('vaccination_cert', None):
                #     application.vaccination_cert = request.FILES.get(
                #         'vaccination_cert', None)
                #     try:
                #         input_pdf = PdfFileReader(application.vaccination_cert)
                #     except utils.PdfReadError:
                #         messages.error(request, 'Unsupported Format or Corrupt PDF for Vaccination Certificate')
                #         return redirect('hab_portal:hab_2')

                # if request.FILES.get('rtpcr_report', None):
                #     application.rtpcr_report = request.FILES.get(
                #         'rtpcr_report', None)
                #     try:
                #         input_pdf = PdfFileReader(application.rtpcr_report)
                #     except utils.PdfReadError:
                #         messages.error(request, 'Unsupported Format or Corrupt PDF for RTPCR Report')
                #         return redirect('hab_portal:hab_2')

                application.save()
                generate_obj_pdf(form_instance.id)
                return redirect('hab_portal:hab_thanks')
            else:
                print(form.errors)
        else:
            form = CampusReturn2022Form2(instance=form_instance)

        return render(request,
                      'forms/hab2.html',
                      {'form': form, 'url': 'form2'})

    except ObjectDoesNotExist:
        return redirect('hab_portal:hab_create')


# @login_required(login_url='/campus_return/accounts/login/')
# def HABDose1Wait(request):
#     return render(request, 'forms/habdose1wait.html')


# @login_required(login_url='/campus_return/accounts/login/')
# def HABEdit(request):
#     form_instance = CampusReturn2022.objects.get(user__user__pk=request.user.id)
#
#     if request.method == 'POST':
#         form = CampusReturn2022Form1(request.POST, request.FILES, instance=form_instance)
#
#         if form.is_valid() and (not form_instance.locked):
#             application = form.save(commit=False)
#             application.user = SiteUser.objects.get(user__pk=request.user.id)
#             application.fee_receipt = request.FILES['fee_receipt']
#             application.save()
#             save_to_user_data(application.user, request.POST, HAB_FIELDS)
#
#             return redirect('hab_portal:hab_thanks')
#
#     else:
#         form = CampusReturn2022Form1(instance=form_instance)
#
#         if form_instance.locked:
#             for field in form.fields:
#                 form.fields[field].disabled = True
#
#     return render(request,
#                   'forms/hab.html',
#                   {'form': form, 'url': 'edit', 'locked': form_instance.locked})


@login_required(login_url='/campus_return/accounts/login/')
def HABThanks(request):
    instance_id = request.session.get('id')
    obj = CampusReturn2022.objects.get(id=instance_id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; inline; filename="somefilename.pdf"'
    buffer = BytesIO()
    pdf1_buffer = obj.final_pdf

    pdf_merger = PdfFileMerger(strict=False)
    try:
        pdf_merger.append(pdf1_buffer, import_bookmarks=False)
    except Exception:
        messages.error(request, 'Unsupported Format or Corrupt PDF')
        return redirect('hab_portal:hab_2')

    if obj.fee_receipt:
        try:
            pdf_merger.append(obj.fee_receipt, import_bookmarks=False)
        except Exception:
            pdf = pikepdf.open(obj.fee_receipt.path,allow_overwriting_input=True)
            pdf.save(obj.fee_receipt.path)
            pdf_merger.append(obj.fee_receipt, import_bookmarks=False)

    try:
        pdf_merger.append(obj.vaccination_cert, import_bookmarks=False)
    except Exception:
        pdf = pikepdf.open(obj.vaccination_cert.path,allow_overwriting_input=True)
        pdf.save(obj.vaccination_cert.path)
        pdf_merger.append(obj.vaccination_cert, import_bookmarks=False)

    if obj.travel_ticket:
        try:
            pdf_merger.append(obj.travel_ticket, import_bookmarks=False)
        except Exception:
            pdf = pikepdf.open(obj.travel_ticket.path,allow_overwriting_input=True)
            pdf.save(obj.travel_ticket.path)
            pdf_merger.append(obj.travel_ticket, import_bookmarks=False)

    # if obj.vaccination_status == "Single Dose":
    if obj.rtpcr_report:
        try:
            pdf_merger.append(obj.rtpcr_report, import_bookmarks=False)
        except Exception:
            pdf = pikepdf.open(obj.rtpcr_report.path,allow_overwriting_input=True)
            pdf.save(obj.rtpcr_report.path)
            pdf_merger.append(obj.rtpcr_report, import_bookmarks=False)
    # else:
    #     messages.error(request, 'Upload a non corrupted pdf of RTPCR Report')
    #     return redirect('hab_portal:hab_2')

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

        url_parameter = request.GET.get("user-input")
        url_param = request.GET.get("sortid")
        url_param2 = request.GET.get("dateOfArrival")
        
        if url_param:
            url_param=url_param
        else:
            url_param="time_of_submission"

        if url_parameter:
            if url_param2: 
                HABforms2 = CampusReturn2022.objects.filter(
                    roll_number__icontains=url_parameter).order_by(url_param)
                HABforms = HABforms2.filter(date_of_arrival__range=[url_param2, url_param2])
            else:
                HABforms = CampusReturn2022.objects.filter(
                    roll_number__icontains=url_parameter).order_by(url_param)

        else:
            if url_param2:
                HABforms2 = CampusReturn2022.objects.all().order_by(url_param)
                HABforms = HABforms2.filter(date_of_arrival__range=[url_param2, url_param2])

            else:
                HABforms = CampusReturn2022.objects.all().order_by(url_param)

        context = {"HABforms": HABforms}

        if request.is_ajax():
            html = render_to_string(
                template_name="hab_portal/partial/partial_entries.html",
                context={"HABforms": HABforms}
            )

            data_dict = {"html_from_view": html}

            return JsonResponse(data=data_dict, safe=False)

        return render(request, 'hab_portal/complete/entries.html', context)
    else:
        return HttpResponseForbidden()

@login_required(login_url='/campus_return/accounts/login/')
def AdminInvited(request):
    if request.user.is_staff:
        url_parameter = request.GET.get("user-input")
        url_param = request.GET.get("sortid")

        if url_param:
            url_param=url_param
        else:
            url_param="time_of_submission"

        if url_parameter:
            HABforms = CampusReturn2022.objects.filter(
                roll_number__icontains=url_parameter).order_by(url_param)

        else:
            HABforms = CampusReturn2022.objects.all().order_by(url_param)

        if request.is_ajax():
            html = render_to_string(
                template_name="hab_portal/partial/partial_invited.html",
                context={"HABforms": HABforms}
            )

            data_dict = {"html_from_view": html}

            return JsonResponse(data=data_dict, safe=False)
        context = {"HABforms": HABforms}
        return render(request, 'hab_portal/complete/invited.html', context)
    else:
        return HttpResponseForbidden()

@login_required(login_url='/campus_return/accounts/login/')
def AdminNotInvited(request):
    if request.user.is_staff:
        url_parameter = request.GET.get("user-input")
        url_param = request.GET.get("sortid")

        if url_param:
            url_param=url_param
        else:
            url_param="time_of_submission"

        if url_parameter:
            HABforms = CampusReturn2022.objects.filter(
                roll_number__icontains=url_parameter).order_by(url_param)

        else:
            HABforms = CampusReturn2022.objects.all().order_by(url_param)

        if request.is_ajax():
            html = render_to_string(
                template_name="hab_portal/partial/partial_not_invited.html",
                context={"HABforms": HABforms}
            )

            data_dict = {"html_from_view": html}

            return JsonResponse(data=data_dict, safe=False)
        context = {"HABforms": HABforms}
        return render(request, 'hab_portal/complete/not_invited.html', context)
    else:
        return HttpResponseForbidden()

def MarkAsInvited(request, id=-1):
    if request.user.is_staff:
        if (id == -1):
            return JsonResponse({'success': False})
        model = CampusReturn2022.objects.get(pk=id)
        model.invite_sent = 'Invited'
        model.save()
        return JsonResponse(data={'success': True})
    else:
        return HttpResponseForbidden()


def MarkAsNotInvited(request, id=-1):
    if request.user.is_staff:
        if (id == -1):
            return JsonResponse({'success': False})
        model = CampusReturn2022.objects.get(pk=id)
        model.invite_sent = 'Not Invited'
        model.save()
        return JsonResponse(data={'success': True})
    else:
        return HttpResponseForbidden()


@login_required(login_url='/campus_return/accounts/login/')
def HABView(request):
    if request.user.is_staff:
        return render(request,
                      'hab_portal/hab-view.html',
                      {'applications': CampusReturn2022.objects.all().order_by('time_of_submission'),
                       'hostels': CampusReturn2022.hostel})
    else:
        return HttpResponseForbidden()


@login_required(login_url='/campus_return/accounts/login/')
def HostelView(request,hostel):
    if request.user.is_staff:
        ctx = {'Hostel':hostel}
        url_parameter = request.GET.get("q")

        if url_parameter:
            HABforms = CampusReturn2022.objects.filter(roll_number__icontains=url_parameter)

        else:
            HABforms = CampusReturn2022.objects.all()

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
            HABforms = CampusReturn2022.objects.filter(roll_number__icontains=url_parameter)

        else:
            HABforms = CampusReturn2022.objects.all()

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
            HABforms = CampusReturn2022.objects.filter(roll_number__icontains=url_parameter)

        else:
            HABforms = CampusReturn2022.objects.all()

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
            HABforms = CampusReturn2022.objects.filter(roll_number__icontains=url_parameter)

        else:
            HABforms = CampusReturn2022.objects.all()
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
        application = CampusReturn2022.objects.get(pk=id)
        application.status = 'Verified'
        application.save()
        return redirect("hab_portal:hostel-view", hostel=hostel)
    else:
        return HttpResponseForbidden()


@login_required(login_url='/campus_return/accounts/login/')
def HostelStatusDecline(request, hostel, id):
    if request.user.is_staff:
        application = CampusReturn2022.objects.get(pk=id)
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
            instance = CampusReturn2022.objects.get(user__user__pk=request.user.id)
            if (instance.proof_of_invitation.name == 'hab_portal/' + file):
                return FileResponse(open('media/hab_portal/' + file, 'rb'))
            else:
                return HttpResponseForbidden()

        if folder == 'fee_recipt':
            instance = CampusReturn2022.objects.get(user__user__pk=request.user.id)
            if (instance.fee_receipt.name == 'hab_portal/' + file):
                return FileResponse(open('media/hab_portal/' + file, 'rb'))
            else:
                return HttpResponseForbidden()

        if folder == 'vaccination':
            instance = CampusReturn2022.objects.get(user__user__pk=request.user.id)
            if (instance.vaccination_cert.name == 'hab_portal/' + file):
                return FileResponse(open('media/hab_portal/' + file, 'rb'))
            else:
                return HttpResponseForbidden()

        if folder == 'rtpcr':
            instance = CampusReturn2022.objects.get(user__user__pk=request.user.id)
            if (instance.rtpcr_report.name == 'hab_portal/' + file):
                return FileResponse(open('media/hab_portal/' + file, 'rb'))
            else:
                return HttpResponseForbidden()

        if folder == 'travel':
            instance = CampusReturn2022.objects.get(user__user__pk=request.user.id)
            if (instance.travel_ticket.name == 'hab_portal/' + file) or request.user.is_staff:
                return FileResponse(open('media/hab_portal/' + file, 'rb'))
            else:
                return HttpResponseForbidden()

        if folder == 'final_pdf':
            instance = CampusReturn2022.objects.get(user__user__pk=request.user.id)
            if (instance.final_pdf.name == 'hab_portal/' + file) or request.user.is_staff:
                return FileResponse(open('media/hab_portal/' + file, 'rb'))
            else:
                return HttpResponseForbidden()

    except:
        return HttpResponseForbidden()


@login_required(login_url='/campus_return/accounts/login/')
def Download_Excel(request, num, Hostel, roll, sort, date):
    if request.user.is_staff:
        response = HttpResponse(content_type='application/ms-excel')

        wb = xlwt.Workbook(encoding='utf-8')

        ws = wb.add_sheet("sheet1")

        row_num = 0

        font_style = xlwt.XFStyle()

        font_style.font.bold = True
        
        if sort:
            sort=sort
        else:
            sort="time_of_submission"

        if roll != 'none':
            if date != 'none': 
                HABforms2 = CampusReturn2022.objects.filter(
                    roll_number__icontains=roll).order_by(sort)
                HABforms = HABforms2.filter(date_of_arrival__range=[date, date])
            else:
                HABforms = CampusReturn2022.objects.filter(
                    roll_number__icontains=roll).order_by(sort)

        else:
            if date != 'none':
                HABforms2 = CampusReturn2022.objects.all().order_by(sort)
                HABforms = HABforms2.filter(date_of_arrival__range=[date, date])

            else:
                HABforms = CampusReturn2022.objects.all().order_by(sort)

        if num == 4 :
            columns = ['Name', 'Roll Number', 'Email','Gender', 'Programme', 'State', 'Time of Submission', 'Arrival Date']
            rows = HABforms.values_list(
            'name', 'roll_number','user__user__email', 'gender','programme', 'returning_from_state', 'time_of_submission', 'date_of_arrival')

        # elif num == 5 :
        #     columns = ['Name', 'Roll Number', 'Email','Gender', 'Programme', 'State', 'Time of Submission', 'Invitation Status']
        #     rows1 = CampusReturn2022.objects.filter(Q(invite_sent='Invited'))
        #     rows = rows1.order_by('time_of_submission').values_list(
        #     'name', 'roll_number','user__user__email', 'gender','programme', 'returning_from_state', 'time_of_submission', 'invite_sent')

        # elif num == 6 :
        #     columns = ['Name', 'Roll Number', 'Email','Gender', 'Programme', 'State', 'Time of Submission', 'Invitation Status']
        #     rows1 = CampusReturn2022.objects.filter(Q(invite_sent='Not Invited'))
        #     rows = rows1.order_by('time_of_submission').values_list(
        #     'name', 'roll_number','user__user__email', 'gender','programme', 'returning_from_state', 'time_of_submission', 'invite_sent')

        elif num == 1  :
            columns = ['Name', 'Roll Number', 'Email','Gender', 'State', 'Hostel', 'Programme', 'Fees', 'Vaccination Status', 'Arrival Date', 'Check-In Date', 'Nature of Testing', 'Mode of Travel', 'Verification Status']
            rows1 = CampusReturn2022.objects.filter(Q(hostel = Hostel))
            rows = rows1.filter(Q(recieved_an_invite='Yes') | Q(vaccination_status='Double Dose')).values_list(
            'name', 'roll_number', 'user__user__email','gender', 'returning_from_state', 'hostel', 'programme', 'mess_fee_paid', 'vaccination_status', 'date_of_arrival', 'check_in_date', 'nature_of_test', 'mode_of_travel','status')

        elif num == 2  :
            columns = ['Name', 'Roll Number', 'Email','Gender', 'State', 'Hostel', 'Programme', 'Fees', 'Vaccination Status', 'Arrival Date', 'Check-In Date', 'Nature of Testing', 'Mode of Travel', 'Verification Status']
            rows1 = CampusReturn2022.objects.filter(Q(hostel = Hostel) & Q(status='Verified'))
            rows = rows1.filter(Q(recieved_an_invite='Yes') | Q(vaccination_status='Double Dose')).values_list(
            'name', 'roll_number', 'user__user__email','gender', 'returning_from_state', 'hostel', 'programme', 'mess_fee_paid', 'vaccination_status', 'date_of_arrival', 'check_in_date', 'nature_of_test', 'mode_of_travel','status')

        elif num == 3  :
            columns = ['Name', 'Roll Number', 'Email','Gender', 'State', 'Hostel', 'Programme', 'Fees', 'Vaccination Status', 'Arrival Date', 'Check-In Date', 'Nature of Testing', 'Mode of Travel', 'Verification Status']
            rows1 = CampusReturn2022.objects.filter(Q(hostel = Hostel) & Q(status='Not Verified'))
            rows = rows1.filter(Q(recieved_an_invite='Yes') | Q(vaccination_status='Double Dose')).values_list(
            'name', 'roll_number', 'user__user__email','gender', 'returning_from_state', 'hostel', 'programme', 'mess_fee_paid', 'vaccination_status', 'date_of_arrival', 'check_in_date', 'nature_of_test', 'mode_of_travel','status')


        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        for row in rows:
            row_num += 1

            for col_num in range(len(row)):
                ws.write(row_num, col_num, str(row[col_num]), font_style)


        response['Content-Disposition'] = 'attachment; filename=Details ' + \
            str(datetime.datetime.now())+'.xls'

        wb.save(response)

        return response

    else:
        return HttpResponseForbidden()
