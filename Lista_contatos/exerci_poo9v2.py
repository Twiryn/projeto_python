from exerci_poo9 import *
from exerci_poo9v3 import *
from display import *
if not Arquivo_Existe():
    Criar_arquivo()
while True:
    try:
     titulos('LISTA DE CONTATOS')
     opçoes()
     linha()
     escolha=int(input('O que gostaria de fazer?:'))
     if escolha == 1:
       titulos('ADICIONAR NOVO CONTATO')
       nome=input('Nome:').upper()
       tel = int(input('Telefone:'))
       email=input('Email:')
       pessoa=Agenda_Contatos(nome,tel,email)
       Adicionar_Contato(pessoa)
     if escolha == 2:
       linha()
       Listar_contatos()
       linha()
     if escolha == 3:
        linha()
        Listar_contatos()
        linha()
        excluir=int(input('Qual contato será removido?'))
        print('Remova usando os indices')
        Remover_contatos(excluir)
     if escolha ==4:
       print('SAINDO DO PROGRAMA...')
       break
    except (TypeError,ValueError):
     print('HOUVE UM ERRO TENTE NOVAMENTE')
    except KeyboardInterrupt:
      print('PROGRAMA ENCERRADO PELO USUARIO')
      break
