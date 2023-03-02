from django.contrib import admin

from .models import Invoice, LineItem

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'customer_email', 'date', 'due_date')
    list_display_links = ('id', 'customer')
    search_fields = ('customer', 'customer_email')
    list_filter = ('customer',)
admin.site.register(Invoice,InvoiceAdmin)


class LineItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'description', 'quantity', 'rate','amount')
    list_display_links = ('id', 'customer')
    search_fields = ('customer', 'customer_email')
    list_filter = ('customer',)
admin.site.register(LineItem,LineItemAdmin)
# Register your models here.
