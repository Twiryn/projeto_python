from BancoDeDados import*
from funcionalidades import *
titulos('BIBLIOTECA LUIZAMANIA')
opc()
escolha=int(input('Qual sera sua opção?'))
if escolha== 1:
    Add_Usuario()
if escolha == 2:
    Add_Livro()