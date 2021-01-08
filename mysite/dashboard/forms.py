from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Claim

class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = [
            'fullname',
            'email',
            'mobile_num',
            'vehicle_model_year',
            'vehicle_model',
            'vehicle_no',
            'accident_dt',
            'location',
            'loss_type',
            'loss_desc',
            'pr_lodged_inq',
            'inq_injury',
            'photo',
            'insurance_cover_note_pdf'
        ]

    def __init__(self, *args, **kwargs):
        super(ClaimForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control field-d'