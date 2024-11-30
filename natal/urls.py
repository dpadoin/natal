from django.urls import path

from . import views
from .views import formulario, sucesso, entrada, teste, visualizar_tabela, salvar_desc, visualizar_tabela2

urlpatterns = [
            path('entrada/', entrada, name='entrada'),
            path('formulario/', formulario, name='formulario'),
            path('sucesso/', sucesso, name='sucesso'),
			path('teste/', teste, name='teste'),
			path('visualizar-tabela/', visualizar_tabela, name='visualizar_tabela'),
			path('visualizar-tabela2/', visualizar_tabela2, name='visualizar_tabela2'),
			path('salvar_desc/', salvar_desc, name='salvar_desc'),
            ]
