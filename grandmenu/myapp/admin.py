from django.contrib import admin

# Register your models here.

from myapp.models import StoreInfo, StoreMenu
admin.site.register(StoreInfo)
admin.site.register(StoreMenu)