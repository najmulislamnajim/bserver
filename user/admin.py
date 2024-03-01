from django.contrib import admin
from .models import UserModel,District,Division

# Register your models here.
admin.site.register(UserModel)
admin.site.register(District)
admin.site.register(Division)