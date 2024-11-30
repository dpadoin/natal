# minha_aplicacao/forms.py
#from django import forms
from django.forms import ModelForm, Textarea
from .models import Pessoa, Descrever, Entrada

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'idade']

class DescreverForm(ModelForm):
    class Meta:
        model = Descrever
        fields = ['quem', 'descricao']
        widgets = {
            "descricao": Textarea(attrs={"cols": 47, "rows": 8}),
        }

class EntradaForm(ModelForm):
    class Meta:
        model = Entrada
        fields = ['chave']
        