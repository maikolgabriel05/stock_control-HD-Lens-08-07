from django import forms
from products.models import Products

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'ncm', 'price', 'stock', 'manufacturing_date']
        widgets = {
            'name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Nome do Produto'}),
            'ncm': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'NCM'}),
            'price': forms.NumberInput(
                attrs={'type': 'number', 'class': 'form-control', 'step': '0.01', 'placeholder': 'Preço do Produto'}),
            'stock': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Quantidade no Estoque'}),
            'manufacturing_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Data de Entrada'}),
        }


    def clean_price(self):
        price = self.cleaned_data['price']
        if price is not None and price < 0:
            raise forms.ValidationError("O preço não pode ser negativo.")
        return price
