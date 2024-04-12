from django.contrib import admin
from .models import InvoiceDetails

# Register your models here.


class InvoiceDetailsAdmin(admin.ModelAdmin):
    list_display = ['documentname', 'centername']  # Fields to display in the admin list view

admin.site.register(InvoiceDetails, InvoiceDetailsAdmin)




