from django.db import models

# Create your models here.
# minha_aplicacao/models.py
#from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

class Descrever(models.Model):
    quem = models.CharField(max_length=100)
    descricao = models.CharField(max_length=256)
    
class Entrada(models.Model):
    chave = models.CharField(max_length=25)
    
class AmigoSecreto(models.Model):
    chave = models.CharField(max_length=25)
    descricao = models.CharField(max_length=256)
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    amigo = models.CharField(max_length=100)

class Teste(models.Model):
    chave = models.CharField(max_length=25)
    nome = models.CharField(max_length=25)
    amigo = models.CharField(max_length=25)
    
class AmigoSecretoTeste2(models.Model):
    chave = models.CharField(max_length=25)
    descricao = models.CharField(max_length=256)
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    amigo = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    enviou_desc = models.CharField(max_length=10)
    enviou_amigo = models.CharField(max_length=10)

  