from django.contrib import admin
from django.urls import path
from .views import InvoiceListView, InvoiceListViewProduct,createInvoiceService,createInvoiceProduct, Sgenerate_PDF, Sview_PDF,Pgenerate_PDF, Pview_PDF

app_name = 'invoice'

urlpatterns = [
    path('', InvoiceListView.as_view(), name="invoice-list"),
    path('invoice-list1/', InvoiceListViewProduct.as_view(), name="invoice-list1"),
    path('create-service/', createInvoiceService, name="invoice-create-service"),
    path('create-product/', createInvoiceProduct, name="invoice-create-product"),
    path('Sinvoice-detail/<id>', Sview_PDF, name='Sinvoice-detail'),
    path('Sinvoice-download/<id>', Sgenerate_PDF, name='Sinvoice-download'),
    path('Pinvoice-detail/<id>', Pview_PDF, name='Pinvoice-detail'),
    path('Pinvoice-download/<id>', Pgenerate_PDF, name='Pinvoice-download')
]


