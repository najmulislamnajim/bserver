from django.contrib import admin
from .models import DonorModel,DonationRequestModel

# Register your models here.
class DonorModelAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','blood_group','last_donate_date']
admin.site.register(DonorModel,DonorModelAdmin)

class DonationRequestModelAdmin(admin.ModelAdmin):
    list_display=['name','email','phone']
admin.site.register(DonationRequestModel,DonationRequestModelAdmin)