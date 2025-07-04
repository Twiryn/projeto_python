from exerci_poo9 import *
from exerci_poo9v3 import *
if not Arquivo_Existe():
    Criar_arquivo()
nome=input('Nome:').upper()
tel = int(input('Telefone:'))
email=input('Email:')
pessoa=Agenda_Contatos(nome,tel,email)

Remover_contatos(1)
Listar_contatos()