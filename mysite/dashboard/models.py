from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.

class Claim(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    mobile_num = PhoneNumberField()

    vehicle_model_year = models.CharField(max_length=6)
    vehicle_model = models.CharField(max_length=60)
    vehicle_no = models.CharField(max_length=20)

    accident_dt = models.DateTimeField()
    location = models.CharField(max_length=80)

    OWN_DAMAGE = 'OD'
    KNOCK_FOR_KNOCK = 'KFK'
    WINDSCREEN_DAMAGE = 'WD'
    THEFT = 'T'
    LOSS_CHOICES = [
        (OWN_DAMAGE, 'Own Damage'),
        (KNOCK_FOR_KNOCK, 'Knock for Knock'),
        (WINDSCREEN_DAMAGE, 'Windscreen Damage'),
        (THEFT, 'Theft'),
    ]

    loss_type = models.CharField(
        max_length=3,
        choices=LOSS_CHOICES,
        default=OWN_DAMAGE,
    )

    loss_desc = models.TextField()
    
    # General Use
    YES = 'Yes'
    NO = 'No'
    
    P_REPORT_CHOICES = [
        (YES, 'Yes'),
        (NO, 'No'),
    ]

    pr_lodged_inq = models.CharField(
        max_length=3,
        choices=P_REPORT_CHOICES,
        default=YES,
    )

    INQ_INJURY_CHOICES = [
        (YES, 'Yes'),
        (NO, 'No'),
    ]

    inq_injury = models.CharField(
        max_length=3,
        choices=INQ_INJURY_CHOICES,
        default=NO,
    )

    def validate_pdf_file_extension(value):
        
        # This try is for django-admin. content type cannot be evaluated because it doesn't exist
        try:
            if value.file.content_type != 'application/pdf':
                raise ValidationError(
                'Invalid file type. Only .pdf files are accepted.'
            )
        except:
            pass
    
    def img_user_directory_path(instance, filename):
        return 'user_{0}/images/{1}'.format(instance.user.username, filename)
    
    def pdf_user_directory_path(instance, filename):
        return 'user_{0}/pdfs/{1}'.format(instance.user.username, filename)
    
    photo = models.ImageField(upload_to=img_user_directory_path)
    insurance_cover_note_pdf = models.FileField(upload_to=pdf_user_directory_path, validators=[validate_pdf_file_extension])
    
    in_p = 'In Progress'
    acp = 'Accepted'

    STATUS_CHOICES = [
        (in_p, 'In Progress'),
        (acp, 'Accepted'),
    ]
    
    status = models.CharField(
        max_length=11,
        choices=STATUS_CHOICES,
        default='In Progress',
    )

