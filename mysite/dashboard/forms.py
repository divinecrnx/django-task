from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Claim

class ClaimForm(forms.Form):
    fullname = forms.CharField(label='Name:', max_length=100)
    email = forms.EmailField(label='Email:', max_length=254)
    mobile_num = PhoneNumberField(label='Mobile Num:')

    vehicle_model_year = forms.CharField(label='Model Year:', max_length=6)
    vehicle_model = forms.CharField(label='Model:', max_length=60)
    vehicle_no = forms.CharField(label='Registration Num:', max_length=20)

    accident_dt = forms.DateTimeField(label='Date and time of accident:')
    location = forms.CharField(label='Location:', max_length=80)
    loss_type = forms.ChoiceField(label='Type of loss:', choices=Claim.LOSS_CHOICES)
    loss_desc = forms.CharField(label='Description of loss:', widget=forms.widgets.Textarea)
    pr_lodged_inq = forms.ChoiceField(label='Police report lodged?', choices=Claim.P_REPORT_CHOICES)
    inq_injury = forms.ChoiceField(label='Anyone else injured?', choices=Claim.INQ_INJURY_CHOICES, initial='No')

    photo = forms.ImageField(label='Photo:')
    insurance_cover_note_pdf = forms.FileField(label='Cover Note: (in PDF)')

    def __init__(self, *args, **kwargs):
        super(ClaimForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control field-d'