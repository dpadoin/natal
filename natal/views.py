# minha_aplicacao/views.py
from django.shortcuts import render, redirect
from .forms import PessoaForm, EntradaForm, DescreverForm
from django.db import models
from .models import Teste, AmigoSecretoTeste2

def entrada(request):
        form = EntradaForm()
        return render(request, 'entrada.html', {'form': form})

def formulario(request):
        req = request.GET
        getcha = req['chave']
        try:                
                dados = AmigoSecretoTeste2.objects.get(chave=getcha)
        except:
                dados = {'autor':'Não Encontrado', 'descricao': '', 'chave': ''}
                
        pessoa = dados.autor
                
        if request.method == 'POST':
                    form = DescreverForm(request.POST)
                    if form.is_valid():
                            form.save()
                            return render(request, 'teste.html')
                    else:
                              return render(request, 'formulario.html', {'form': form})  
        else:
                    form = DescreverForm(instance=dados)
                    return render(request, 'formulario.html', {'form': form, 'pessoa': pessoa, 'chave': getcha})

def sucesso(request):
        return render(request, 'sucesso.html')

def teste(request):
        req = request.GET
        getcha = req['chave']
        try:                
                dados = Teste.objects.get(chave=getcha)
        except:
                dados = {'nome':'Não Encontrado'}        
        return render(request, 'teste.html', {'dados': dados, 'getcha': getcha})

def visualizar_tabela(request):
    dados_tabela = AmigoSecretoTeste2.objects.all()  # Obtém todos os objetos da tabela
    return render(request, 'tabela.html', {'dados_tabela': dados_tabela})

def visualizar_tabela2(request):
    dados_tabela = AmigoSecretoTeste2.objects.all()  # Obtém todos os objetos da tabela
    return render(request, 'tabela2.html', {'dados_tabela': dados_tabela,})

def salvar_desc(request):
        req = request.POST
        desc = req['descricao']
        getcha = req['chave']
        
        ast = AmigoSecretoTeste2.objects.get(chave=getcha)
        ast.descricao = desc
        ast.enviou_desc = str(len(desc))
        ast.save(update_fields=['descricao', 'enviou_desc'])
        
        return render(request, 'sucesso.html')
