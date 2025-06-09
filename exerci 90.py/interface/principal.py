from tela import *
from arquivo import *
from time import sleep
arq='miguel.txt'
if not arquivo_existe(arq):
    criar_arquivo(arq)
while True:
    escolha=menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema'])
    if escolha == 1:
       #Opção de listar o conteudo de um arquivo
       ler_arquivo(arq)
    elif escolha == 2:
        #opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome=input('Nome: ')
        idade=leia_int('Idade:')
        adicionar(arq,nome,idade)
    elif escolha ==3:
        cabeçalho('\033[32m>>SAINDO DO SISTEMA, VOLTE SEMPRE<<\033[m')
        break
    else:
        print(f'\033[31mERRO! Digite uma opção valida\033[m')
    sleep(1.0) 
