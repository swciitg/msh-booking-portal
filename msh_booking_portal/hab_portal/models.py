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
    ('dibang', 'Dibang'),
    ('disang', '*Disang'),
    ('kameng', 'Kameng'),
    ('umiam', 'Umiam'),
    ('barak', 'Barak'),
    ('kapili', 'Kapili'),
    ('dihing', 'Dihing'),
    ('subansiri', 'Subansiri'),
    ('dhansiri', 'Dhansiri'),
    ('dibang', 'Dibang'),
    ('msh', 'Married Scholar Hostel'),
    ('not-alloted', 'Not Alloted'),
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
    ('Verified', 'Verified'),
    ('Not Verified', 'Not Verified'),
]

INVITED = [
    ('Invited', 'Invited'),
    ('Not Invited', 'Not Invited'),
]

VACCINATION_STATUS_CHOICES = [
    ('Single Dose', 'Single Dose'),
    ('Double Dose', 'Double Dose'),
]

REGISTERED_FOR_SESSION =[
     ('Yes', 'Yes'),
     ('No', 'No'),
]

RECIEVED_AN_INVITE =[
     ('Yes', 'Yes'),
     ('No', 'No'),
]

PROGRAMMES =[ ('B.Tech','B.Tech'),
             ('B.Des','B.Des'),
             ('M.Tech','M.Tech'),
             ('M.Des','M.Des'),
             ('M.A.','M.A.'),
             ('M.Sc.','M.Sc.'),
             ('MSR','MSR'),
             ('PHD/IPDF','PHD/IPDF'),
             ('Project Staff','Project Staff'),]

STATE_CHOICES = [("Other (Foreign Country)", "Other (Foreign Country)"),
                 ("Andhra Pradesh","Andhra Pradesh"),
                 ("Arunachal Pradesh ","Arunachal Pradesh "),
                 ("Assam","Assam"),
                 ("Bihar","Bihar"),
                 ("Chhattisgarh","Chhattisgarh"),
                 ("Goa","Goa"),
                 ("Gujarat","Gujarat"),
                 ("Haryana","Haryana"),
                 ("Himachal Pradesh","Himachal Pradesh"),
                 ("Jammu and Kashmir ","Jammu and Kashmir "),
                 ("Jharkhand","Jharkhand"),
                 ("Karnataka","Karnataka"),
                 ("Kerala","Kerala"),
                 ("Madhya Pradesh","Madhya Pradesh"),
                 ("Maharashtra","Maharashtra"),
                 ("Manipur","Manipur"),
                 ("Meghalaya","Meghalaya"),
                 ("Mizoram","Mizoram"),
                 ("Nagaland","Nagaland"),
                 ("Odisha","Odisha"),
                 ("Punjab","Punjab"),
                 ("Rajasthan","Rajasthan"),
                 ("Sikkim","Sikkim"),
                 ("Tamil Nadu","Tamil Nadu"),
                 ("Telangana","Telangana"),
                 ("Tripura","Tripura"),
                 ("Uttar Pradesh","Uttar Pradesh"),
                 ("Uttarakhand","Uttarakhand"),
                 ("West Bengal","West Bengal"),
                 ("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
                 ("Chandigarh","Chandigarh"),
                 ("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),
                 ("Daman and Diu","Daman and Diu"),
                 ("Lakshadweep","Lakshadweep"),
                 ("Delhi","Delhi"),
                 ("Puducherry","Puducherry")]

def proof_of_invitation_file_name(instance, filename):
    return 'hab_portal/proof_of_invitation/{0}{1}'.format(instance.user.pk, os.path.splitext(filename)[-1])

def final_pdf_file_name(instance, filename):
    return 'hab_portal/final_pdf/{0}.pdf'.format(instance.user.pk)

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
    if os.path.splitext(value.name)[-1].lower() == '.pdf':
        return value
    else:
        raise ValidationError('Upload a PDF File.')


def validate_file_extension_image(value):
    if os.path.splitext(value.name)[-1].lower() in ['.jpg', '.jpeg', '.png']:
        return value
    else:
        print(os.path.splitext(value.name)[-1])
        raise ValidationError('Upload an image file.')

def get_current_date():
    return datetime.now().strftime('%Y-%m-%d')



def validate_digit_length(phone):
    if not (phone.isdigit() and len(phone) == 9):
        raise ValidationError('Roll Number must be of 9 digits')







HAB_FIELDS = {'roll_number': 'roll_number',
               }




class HABModel(models.Model):
    # Invisible Fields

    time_of_submission = models.DateTimeField(auto_now_add=True, null=True)
    invite_sent = models.CharField(max_length=256, choices=INVITED, default='Not Invited', null=True)
    status = models.CharField(max_length=256, choices=STATUS, default='Not Verified', null=True)
    locked = models.BooleanField(default=False)

    # Personal Details
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE, null=True)
    name = models.CharField('Name', max_length=256)
    roll_number = models.CharField('Roll No.', max_length=100,help_text='Enter a valid 9 digit Roll Number.',validators=[validate_digit_length] )
    gender = models.CharField('Gender', choices=GENDERS, max_length=256, default='Male')
    email = models.CharField('Email', max_length=256)
    mobile = models.IntegerField('Mobile')
    vaccination_status = models.CharField('Vaccination Status', max_length=256,
                                          choices=VACCINATION_STATUS_CHOICES, null=True, default='Single Dose')

    programme = models.CharField('Programme', max_length=256, choices=PROGRAMMES)
    department = models.CharField('Department', max_length=256)
    supervisor = models.CharField('Supervisor (if any)', max_length=256, blank=True)
    email_of_supervisor = models.CharField('Supervisor Email', max_length=256, blank=True)


    returning_from_state = models.CharField('Returning from (state)', max_length=256, null=True, choices=STATE_CHOICES)

    #dose1 Details
    recieved_an_invite=models.CharField('Have you Recieved an Invite', max_length=256,
                                          choices=RECIEVED_AN_INVITE, null=True, default='No')
    proof_of_invitation = models.FileField('Proof of Invitation', upload_to=proof_of_invitation_file_name, storage=OverwriteStorage(),
                                            validators=[validate_file_size, validate_file_extension_image],
                                            help_text='Upload screenshot of mail received from student affairs. Upload an image file of .jpg, .jpeg or .png extension.',
                                            null=True, blank=True)

    # Return Details
    date_of_arrival = models.DateTimeField('Date of Arrival', default=datetime.now, null=True)
    mode_of_travel = models.CharField('Mode of Travel', blank=True, max_length=256, null=True)
    flight_train_number = models.CharField('Flight / Train No.', blank=True, max_length=256, null=True)

    # Test Details
    nature_of_test = models.CharField('Nature of Test', choices=NATURES_OF_TEST, max_length=256, null=True, default='RT-PCR')
    date_of_testing = models.DateField('Date of Test', default=datetime.now, null=True)

    # Hostel Related Information
    hostel = models.CharField('Hostel', max_length=256, choices=HOSTELS, null=True)
    room_no = models.CharField('Room Number', max_length=256, blank=True, null=True)
    check_in_date = models.DateTimeField('Check-in Date', default=datetime.now, null=True)

    # Status of Payment
    mess_fee_paid = models.IntegerField('Fee Paid', null=True)
    date_of_payment = models.DateField('Date of Payment', default=datetime.now, null=True)

    # Enclosures
    fee_receipt = models.FileField('Fee Receipt', upload_to=fee_upload_file_name, storage=OverwriteStorage(),
                                   validators=[validate_file_size, validate_file_extension],
                                   help_text='Upload a .PDF file not greater than 10 MB in size.', null=True, blank=True)

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
                                    help_text='Upload a .PDF file not greater than 10 MB in size.', null=True, blank=True)

    final_pdf = models.FileField('final pdf',upload_to=final_pdf_file_name,storage=OverwriteStorage(), null=True)


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
            ('can_view_dibang_hostel_data', 'can view dibang hostel data'),
            ('can_view_suban_hostel_data', 'can view subansiri hostel data'),
            ('can_view_dhan_hostel_data', 'can view dhansiri hostel data'),
            ('can_view_msh_hostel_data', 'can view msh hostel data'),
            ('can_view_not_alloted_data', 'can view not alloted data'),
        )

    def __str__(self):
        return self.user.user.first_name+" "+self.user.user.last_name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in HABModel._meta.fields]

    def clean(self):
        if (self.recieved_an_invite == 'Yes') and (self.proof_of_invitation.name == ''):
            raise ValidationError({'proof_of_invitation': 'Proof of invitation not submitted.'})

    def get_final_pdf_url(self):
        try:
            return self.final_pdf.url
        except:
            print('-> Final PDF is missing for:', self.user.user.id, self.name)
            return ''
