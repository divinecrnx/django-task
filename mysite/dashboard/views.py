from django.shortcuts import render, redirect
from .forms import ClaimForm
from .models import Claim
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib import messages
from django.urls import reverse
from pathlib import Path

# Create your views here.

def index(request):
    return render(request, 'dashboard/dashboard.html')

def submit(request):

    def handle_uploaded_file(f, f_type, filename):

        output = Path(__file__).resolve().parent.parent / 'media' / f_type / filename

        with open(output, 'wb') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
    
    if request.method == 'POST':
        form = ClaimForm(request.POST, request.FILES)

        if form.is_valid():
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
            handle_uploaded_file(request.FILES['photo'], 'images', photo.name)
            handle_uploaded_file(request.FILES['insurance_cover_note_pdf'], 'pdfs', insurance_cover_note_pdf.name)
            claim.save()           

            messages.success(request, 'Claim submitted!')
            return redirect(reverse('dashboard:index'))
    else:
        form = ClaimForm()

    
    return render(request, 'dashboard/submit.html', {'form': form})

def manage(request):
    return render(request, 'dashboard/manage.html')