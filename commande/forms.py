from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['Repas', 'Quantité','Numéro_de_téléphone']

def clean_quantity(self):
        quantity = self.cleaned_data.get('Quantité')
        if quantity <= 0:
            raise forms.ValidationError("La quantité doit être supérieure à zéro.")
        return quantity