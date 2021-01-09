from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.contrib import messages
from django.urls import reverse
from django.views import generic
from .forms import ClaimForm
from .models import Claim
from pathlib import Path


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'dashboard/dashboard.html'
    context_object_name = 'claims'

    def get_queryset(self):

        return Claim.objects.filter(
            user=self.request.user
        ).order_by('-id')

def query_claim(request, form):
    
    fullname = form.cleaned_data['fullname']
    email = form.cleaned_data['email']
    mobile_num = form.cleaned_data['mobile_num']
    vehicle_model_year = form.cleaned_data['vehicle_model_year']
    vehicle_model = form.cleaned_data['vehicle_model']
    vehicle_no = form.cleaned_data['vehicle_no']
    accident_dt = form.cleaned_data['accident_dt']
    location = form.cleaned_data['location']
    loss_type = form.cleaned_data['loss_type']
    loss_desc = form.cleaned_data['loss_desc']
    pr_lodged_inq = form.cleaned_data['pr_lodged_inq']
    inq_injury = form.cleaned_data['inq_injury']
    photo = form.cleaned_data['photo']
    insurance_cover_note_pdf = form.cleaned_data['insurance_cover_note_pdf']

    claim = Claim(
        user=request.user,
        fullname=fullname,
        email=email,
        mobile_num=mobile_num,
        vehicle_model_year=vehicle_model_year,
        vehicle_model=vehicle_model,
        vehicle_no=vehicle_no,
        accident_dt=accident_dt,
        location=location,
        loss_type=loss_type,
        loss_desc=loss_desc,
        pr_lodged_inq=pr_lodged_inq,
        inq_injury=inq_injury,
        photo=photo,
        insurance_cover_note_pdf=insurance_cover_note_pdf,
    )
    claim.save()
    
    messages.success(request, 'Claim submitted!')

@login_required
def submit(request):
    
    if request.method == 'POST':
        form = ClaimForm(request.POST, request.FILES)

        if form.is_valid():
            query_claim(request, form)
        
        return redirect(reverse('dashboard:index'))    
    else:
        form = ClaimForm()

    
    return render(request, 'dashboard/submit.html', {'form': form, 'f_type': 'Submit'})

@login_required
def manage(request, claim_id):
    data = Claim.objects.get(id=claim_id)
    form = ClaimForm(model_to_dict(data))

    return render(request, 'dashboard/manage.html', {'form': form, 'f_type': 'Manage'})