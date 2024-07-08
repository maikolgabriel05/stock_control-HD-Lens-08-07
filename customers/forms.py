from django import forms
from django.core.exceptions import ValidationError
from django_cpf_cnpj.validators import validate_cpf, validate_cnpj
from .models import Customers

class CustomerForm(forms.ModelForm):
    cnpj = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'CNPJ/CPF do Cliente'}))

    class Meta:
        model = Customers
        fields = ['name', 'cnpj', 'email', 'state', 'city', 'address']
        error_messages = {
            'email': {'invalid': 'Por favor, insira um endereço de e-mail válido.'},
        }
        widgets = {
            'name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Nome do cliente'}),
            'email': forms.EmailInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'E-mail'}),
            'state': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Estado'}),
            'city': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Cidade'}),
            'address': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Endereço'}),
        }

    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')

        if not cnpj:
            return cnpj  # Se estiver vazio, a validação do CharField irá lidar com isso

        cnpj = ''.join(filter(str.isdigit, cnpj))  # Remove caracteres não numéricos

        if len(cnpj) == 11:
            try:
                validate_cpf(cnpj)
            except ValidationError:
                raise ValidationError('Por favor, insira um CPF válido.')
        elif len(cnpj) == 14:
            try:
                validate_cnpj(cnpj)
            except ValidationError:
                raise ValidationError('Por favor, insira um CNPJ válido.')
        else:
            raise ValidationError('Por favor, insira um CPF ou CNPJ válido.')

        return cnpj
