from django.contrib import admin
from forms_atelier.models import data

class DataAdmin(admin.ModelAdmin):
    list_display = ('manager', 'lastName', 'firstName','middleName', 'measurements', 'fabricType','deliveryOption')
    list_editable = ('lastName', 'firstName','middleName', 'measurements', 'fabricType','deliveryOption')
    list_filter = ('manager', 'lastName', 'firstName','middleName', 'measurements', 'fabricType','deliveryOption')

admin.site.register(data, DataAdmin)