from django.contrib import admin
from .models import NewsModel

# Register your models here.
class NewsModelAdmin(admin.ModelAdmin):
    list_display=['title','editor','created_date']
admin.site.register(NewsModel,NewsModelAdmin)