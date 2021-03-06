from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from .models import Claim
from django.contrib.auth.models import User
import datetime, pytz

# Create your tests here.

class DashboardViewTests(TestCase):

    def setUp(self):
        self.client.force_login(User.objects.create_user(username='upa', password='1234'))

    def create_claim(self):
        tz = pytz.timezone('Asia/Kuala_Lumpur')

        return Claim.objects.create(
            user = User.objects.get(username='upa'),
            fullname='fullname',
            email='email@email.com',
            mobile_num='+60123456789',
            vehicle_model_year='MY2020',
            vehicle_model='Proton Persona',
            vehicle_no='ABC 123',
            accident_dt=datetime.datetime(2021, 1, 1, 16, 0, 0, tzinfo=tz),
            location='Kuala Lumpur',
            loss_type='OD',
            loss_desc='Some desc',
            pr_lodged_inq='Yes',
            inq_injury='Yes',
            photo=SimpleUploadedFile('test.png', content='', content_type='image/png'),
            insurance_cover_note_pdf=SimpleUploadedFile('test.pdf', content='', content_type='application/pdf'),
        )

    def manage_claim(self):
        edit_claim = self.create_claim()
        edit_claim.vehicle_no = 'DEF 456'
        edit_claim.save()

    def delete_claim(self):
        del_claim = self.create_claim()
        del_claim.delete()
    
    def test_login_requirement(self):
        response = self.client.get(reverse('dashboard:index'))
        self.assertEqual(response.status_code, 200)

    def test_login_redirect(self):
        self.client.logout()
        response = self.client.get(reverse('dashboard:index'))
        self.assertEqual(response.status_code, 302)

    def test_no_claim(self):
        response = self.client.get(reverse('dashboard:index'))
        self.assertQuerysetEqual(response.context['claims'], [])

    def test_yes_claim(self):
        self.create_claim()
        response = self.client.get(reverse('dashboard:index'))
        self.assertQuerysetEqual(
            response.context['claims'],
            ['<Claim: ABC 123 - Proton Persona>']
        )

    def test_edit_claim(self):
        self.manage_claim()
        response = self.client.get(reverse('dashboard:index'))
        self.assertQuerysetEqual(
            response.context['claims'],
            ['<Claim: DEF 456 - Proton Persona>']
        )

    def test_delete_claim(self):
        x = self.create_claim()
        response = self.client.get(reverse('dashboard:index'))
        self.assertQuerysetEqual(
            response.context['claims'],
            ['<Claim: ABC 123 - Proton Persona>']
        )
        x.delete()
        response = self.client.get(reverse('dashboard:index'))
        self.assertQuerysetEqual(response.context['claims'], [])
