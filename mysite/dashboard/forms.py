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

    def clean_insurance_cover_note_pdf(self):
        file = self.cleaned_data.get('insurance_cover_note_pdf')
        if not file.content_type == 'application/pdf':
            raise forms.ValidationError('File must be a PDF document.')
        else:
            return file

    def __init__(self, *args, **kwargs):
        super(ClaimForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control field-d'

class ManageClaimForm(ClaimForm):
    class Meta:
        model = Claim
        exclude = (
            'user',
            'photo',
            'insurance_cover_note_pdf',
            'status',
        )

class ManageClaimPhotoForm(ClaimForm):
    class Meta:
        model = Claim
        fields = (
            'photo',
        )

class ManageClaimInsForm(ClaimForm):
    class Meta:
        model = Claim
        fields = (
            'insurance_cover_note_pdf',
        )