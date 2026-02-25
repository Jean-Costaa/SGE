from django import forms
from . import models


class BrandForme(forms.ModelForm):

    class Meta:
        model = models.Brand
        fields = ['name', 'description']
