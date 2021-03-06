from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict
from django.contrib import messages
from django.urls import reverse
from django.views import generic
from .forms import ClaimForm, ManageClaimForm, ManageClaimPhotoForm, ManageClaimInsForm
from .models import Claim
from pathlib import Path

# Create your views here.

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'dashboard/dashboard.html'
    context_object_name = 'claims'

    def get_queryset(self):

        return Claim.objects.filter(
            user=self.request.user
        ).order_by('-id')

@login_required
def submit(request):
    
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
            return redirect(reverse('dashboard:index'))    
    else:
        form = ClaimForm()
    
    return render(request, 'dashboard/submit.html', {'form': form, 'f_type': 'Submit'})

@login_required
def manage(request, claim_id):

    data = Claim.objects.get(id=claim_id)

    get_form = ClaimForm(model_to_dict(data), use_required_attribute=False)
    get_form_photo = ManageClaimPhotoForm()
    get_form_ins = ManageClaimInsForm()

    context = {
        'form': get_form,
        'form_photo': get_form_photo,
        'form_ins': get_form_ins,
        'f_type': 'Manage',
        'cid': claim_id,
        'link': data,
    }
    
    if request.method == 'POST':
        post_form = ManageClaimForm(request.POST)
        post_form_photo = ManageClaimPhotoForm(request.POST, request.FILES)
        post_form_ins = ManageClaimInsForm(request.POST, request.FILES)

        if post_form.is_valid():
            data.fullname = post_form.cleaned_data['fullname']
            data.email = post_form.cleaned_data['email']
            data.mobile_num = post_form.cleaned_data['mobile_num']
            data.vehicle_model_year = post_form.cleaned_data['vehicle_model_year']
            data.vehicle_model = post_form.cleaned_data['vehicle_model']
            data.vehicle_no = post_form.cleaned_data['vehicle_no']
            data.accident_dt = post_form.cleaned_data['accident_dt']
            data.location = post_form.cleaned_data['location']
            data.loss_type = post_form.cleaned_data['loss_type']
            data.loss_desc = post_form.cleaned_data['loss_desc']
            data.pr_lodged_inq = post_form.cleaned_data['pr_lodged_inq']
            data.inq_injury = post_form.cleaned_data['inq_injury']

            messages.success(request, 'Claim updated!')
            data.save()

            return redirect(reverse('dashboard:manage', args=(claim_id,)))
        else:
            if not len(post_form.data) == 1:
                context['form'] = post_form
                print("form ran")
                return render(request, 'dashboard/manage.html', context)

        if post_form_photo.is_valid():
            data.photo.delete()
            data.photo = post_form_photo.cleaned_data['photo']
            
            messages.success(request, 'Claim updated!')
            data.save()

            return redirect(reverse('dashboard:manage', args=(claim_id,)))
        else:
            p_error = post_form_photo.errors.get_json_data()['photo'][0]['message']

            if not p_error == 'This field is required.':
                context['form_photo'] = post_form_photo
                return render(request, 'dashboard/manage.html', context)

        if post_form_ins.is_valid():
            data.insurance_cover_note_pdf.delete()
            data.insurance_cover_note_pdf = post_form_ins.cleaned_data['insurance_cover_note_pdf']
            
            messages.success(request, 'Claim updated!')
            data.save()

            return redirect(reverse('dashboard:manage', args=(claim_id,)))
        else:
            i_error = post_form_ins.errors.get_json_data()['insurance_cover_note_pdf'][0]['message']

            if not i_error == 'This field is required.':
                context['form_ins'] = post_form_ins
                return render(request, 'dashboard/manage.html', context)
    else:
        if data.status == 'Accepted':
            return render(request, 'dashboard/view_claim.html', {'claim': data})
        else:
            return render(request, 'dashboard/manage.html', context)

@login_required
def delete(request, claim_id):
    
    claim = Claim.objects.get(id=claim_id)
    if claim.status == 'In Progress':
        claim.delete()

    return redirect(reverse('dashboard:index'))