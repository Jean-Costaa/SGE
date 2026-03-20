from django import forms
from django.core.exceptions import ValidationError
from . import models


class OutflowForme(forms.ModelForm):

    class Meta:
        model = models.Outflow
        fields = ['product', 'quantity', 'descripition']
        widgets = {
            'product': forms.Select({'class': 'form-control'}),
            'quantity': forms.NumberInput({'class': 'form-control'}),
            'descripition': forms.Textarea({'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'product': 'Produto',
            'quantity': 'Quantidade',
            'descripition': 'Descrição',
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')

        if quantity > product.quantity:
            raise ValidationError(
                f'A quantidade disponível em estoque para o produto {product.title} e de {product.quantity} unidades.'
            )

        return quantity
