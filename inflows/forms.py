from django import forms
from . import models


class InflowForme(forms.ModelForm):

    class Meta:
        model = models.Inflow
        fields = ['supplier', 'product', 'quantity', 'descripition']
        widgets = {
            'supplier': forms.Select({'class': 'form-control'}),
            'product': forms.Select({'class': 'form-control'}),
            'quantity': forms.NumberInput({'class': 'form-control'}),
            'descripition': forms.Textarea({'class': 'form-control', 'rows':3}),
        }
        labels = {
            'supplier': 'Fornecedor',
            'product': 'Produto',
            'quantity': 'Quantidade',
            'descripition': 'Descrição',
        }
