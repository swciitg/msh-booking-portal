import os
from django.db import models
from django.core.exceptions import ValidationError
from users.models import SiteUser
from .storage import OverwriteStorage
from datetime import datetime


HOSTELS = [
    ('lohit', 'Lohit'),
    ('brahmaputra', 'Brahmaputra'),
    ('siang', 'Siang'),
    ('manas', 'Manas'),
    ('disang', 'Disang'),
    ('kameng', 'Kameng'),
    ('umiam', 'Umiam'),
    ('barak', 'Barak'),
    ('kapili', 'Kapili'),
    ('dihing', 'Dihing'),
    ('subansiri', 'Subansiri'),
    ('dhansiri', 'Dhansiri'),
    ('msh', 'Married Scholar Hostel'),
]

GENDERS = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

NATURES_OF_TEST = [
    ('RT-PCR', 'RT-PCR'),
    ('TrueNat', 'TrueNat')
]

STATUS = [
    ('Accepted', 'Accepted'),
    ('Pending', 'Pending'),
    ('Declined', 'Declined'),
]

VACCINATION_STATUS_CHOICES = [
    ('Single Dose', 'Single Dose'),
    ('Double Dose', 'Double Dose'),
]

REGISTERED_FOR_SESSION =[
     ('Yes', 'Yes'),
     ('No','No'),
]

RECIEVED_AN_INVITE =[
     ('Yes', 'Yes'),
     ('No','No'),
]

def fee_upload_file_name(instance, filename):
    return 'hab_portal/fee_recipt/{0}.pdf'.format(instance.user.pk)

def vacc_upload_file_name(instance, filename):
    return 'hab_portal/vaccination/{0}.pdf'.format(instance.user.pk)

def travel_upload_file_name(instance, filename):
    return 'hab_portal/travel/{0}.pdf'.format(instance.user.pk)

def rtpcr_upload_file_name(instance, filename):
    return 'hab_portal/rtpcr/{0}.pdf'.format(instance.user.pk)


def validate_file_size(value):
    size = value.size

    if size <= 10*1024**2:
        return value
    else:
        raise ValidationError('The maximum file size is 10 MB.')


def validate_file_extension(value):
    if os.path.splitext(value.name)[-1] == '.pdf':
        return value
    else:
        raise ValidationError('Upload a PDF File.')


def get_current_date():
    return datetime.now().strftime('%Y-%m-%d')


HAB_FIELDS = {'roll_number': 'roll_number',
              }


class HABModel(models.Model):
    # Invisible Fields
    time_of_submission = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=256, choices=STATUS, default='Pending', null=True)
    locked = models.BooleanField(default=False)

    # Personal Details
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=256)
    roll_number = models.CharField('Roll No.', max_length=256)
    gender = models.CharField('Gender', choices=GENDERS, max_length=256)
    email = models.EmailField('Email', max_length=256)
    mobile = models.CharField('Mobile', max_length=256)
    department = models.CharField('Department', max_length=256)
    programme = models.CharField('Programme', max_length=256)
    supervisor = models.CharField('Supervisor (if any)', max_length=256, blank=True)
    email_of_supervisor = models.EmailField('Supervisor Email', max_length=256, blank=True)

    registered_for_academic_semester = models.CharField('Registered for Academic Semester',choices=REGISTERED_FOR_SESSION, max_length=3)
    vaccination_status = models.CharField('Vaccination Status', max_length=256,
                                          choices=VACCINATION_STATUS_CHOICES, null=True)
    #dose1 Details
    recieved_an_invite=models.CharField('Have you Recieved an Invite', max_length=256,
                                          choices=RECIEVED_AN_INVITE, null=True)
    proof_of_invitation = models.FileField('Proof of Invitation', upload_to=fee_upload_file_name, storage=OverwriteStorage(),
                                   validators=[validate_file_size, validate_file_extension],
                                   help_text='Upload a .PDF file not greater than 10 MB in size.', null=True)

    # Return Details
    returning_from_state = models.CharField('Returning from (state)', max_length=256, null=True)
    date_of_arrival = models.DateTimeField('Date of Arrival', default=datetime.now, null=True)
    mode_of_travel = models.CharField('Mode of Travel', blank=True, max_length=256, null=True)
    flight_train_number = models.CharField('Flight / Train No.', blank=True, max_length=256, null=True)

    # Test Details
    nature_of_test = models.CharField('Nature of Test', choices=NATURES_OF_TEST, max_length=256, null=True)
    date_of_testing = models.DateField('Date of Test', default=datetime.now, null=True)

    # Hostel Related Information
    hostel = models.CharField('Hostel', max_length=256, choices=HOSTELS, null=True)
    room_no = models.CharField('Room Number', max_length=256, blank=True, null=True)
    check_in_date = models.DateTimeField('Check-in Date', default=datetime.now, null=True)

    # Status of Payment
    mess_fee_paid = models.IntegerField('Fee Paid', null=True)
    date_of_payment = models.DateField('Date of Payment', null=True)

    # Enclosures
    fee_receipt = models.FileField('Fee Receipt', upload_to=fee_upload_file_name, storage=OverwriteStorage(),
                                   validators=[validate_file_size, validate_file_extension],
                                   help_text='Upload a .PDF file not greater than 10 MB in size.', null=True)

    vaccination_cert = models.FileField('Vaccination Certificate', upload_to=vacc_upload_file_name,
                                        storage=OverwriteStorage(),
                                        validators=[validate_file_size, validate_file_extension],
                                        help_text='Upload a .PDF file not greater than 10 MB in size.', null=True)

    travel_ticket = models.FileField('Travel Ticket', upload_to=travel_upload_file_name,
                                    storage=OverwriteStorage(),
                                    validators=[validate_file_size, validate_file_extension],
                                    help_text='Upload a .PDF file not greater than 10 MB in size.', null=True)

    rtpcr_report = models.FileField('RTPCR Report', upload_to=rtpcr_upload_file_name,
                                    storage=OverwriteStorage(),
                                    validators=[validate_file_size, validate_file_extension],
                                    help_text='Upload a .PDF file not greater than 10 MB in size.', null=True)


    class Meta:
        ordering = ['hostel', '-status','date_of_arrival']
        permissions = (
            ('can_view_lohit_hostel_data', 'can view lohit hostel data'),
            ('can_view_brahma_hostel_data', 'can view brahma hostel data'),
            ('can_view_siang_hostel_data', 'can view siang hostel data'),
            ('can_view_manas_hostel_data', 'can view manas hostel data'),
            ('can_view_disang_hostel_data', 'can view disang hostel data'),
            ('can_view_kameng_hostel_data', 'can view kameng hostel data'),
            ('can_view_umiam_hostel_data', 'can view umiam hostel data'),
            ('can_view_barak_hostel_data', 'can view barak hostel data'),
            ('can_view_kapili_hostel_data', 'can view kapili hostel data'),
            ('can_view_dihing_hostel_data', 'can view dihing hostel data'),
            ('can_view_suban_hostel_data', 'can view subansiri hostel data'),
            ('can_view_dhan_hostel_data', 'can view dhansiri hostel data'),
            ('can_view_msh_hostel_data', 'can view msh hostel data'),
        )

    def __str__(self):
        return self.user.user.first_name+" "+self.user.user.last_name
