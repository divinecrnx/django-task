from django import forms
from django.core.exceptions import ValidationError

class UserSignupForm(forms.Form):
    username = forms.CharField(label='Username:', max_length=30)
    email = forms.EmailField(label='Email:', max_length=254)
    password = forms.CharField(label='Password:', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm password:', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if not password == confirm_password:
            raise ValidationError(
                "Passwords do not match."
        )