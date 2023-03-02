from django import forms
from django.forms import formset_factory
from .models import Invoice

class InvoiceForm(forms.Form):
    
        # fields = ['customer', 'message']
    customer = forms.CharField(
        label='Cusomter',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Customer/Company Name',
            'rows':1
        })
    )
    customer_email = forms.CharField(
        label='Customer Email/Phone',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email/Phone',
            'rows':1
        }),
        required=False

    )
    billing_address = forms.CharField(
        label='Billing Address',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '',
            'rows':1
        }),
        required=False

    )
    message = forms.CharField(
        label='Message/Note',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'message',
            'rows':1
        }),
        required=False

    )

class LineItemForm(forms.Form):
    
    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(attrs={
            'class': 'form-control input',
            'placeholder': 'Enter service here',
            "rows":1
        })
    )
    quantity = forms.IntegerField(
        label='Qty',
        widget=forms.NumberInput(attrs={
            'class': 'form-control input quantity',
            'placeholder': 'Quantity'
        }) #quantity should not be less than one
    )
    rate = forms.DecimalField(
        label='Rate $',
        widget=forms.NumberInput(attrs={
            'class': 'form-control input rate',
            'placeholder': 'Rate',
        })
    )
    # amount = forms.DecimalField(
    #     disabled = True,
    #     label='Amount $',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control input',
    #     })
    # )
    
LineItemFormset = formset_factory(LineItemForm, extra=1)


