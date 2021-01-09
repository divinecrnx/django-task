from django.contrib import admin
from .models import Claim

# Register your models here.

class ClaimAdmin(admin.ModelAdmin):
    list_display = ('vehicle_no', 'loss_type', 'accident_dt', 'location')
    search_fields = ['user__username']
    list_filter = ['user', 'loss_type']

admin.site.register(Claim, ClaimAdmin)