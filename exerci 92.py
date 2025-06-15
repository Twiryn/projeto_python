from random import randint
from time import sleep
def linhas(tam=42):
    print ('-' * tam)
def titulos(txt):
    print('-'*42)
    print(txt.center(42))
    print('-'*42)
titulos('JOGO DE ADIVINHAÇÃO')
print('O jogo consiste em escolher um numero \nque foi sorteado pelo computador em um intervalo de numeros')
linhas()
print('DIFICULDADES:')
print('\033[33m1-NORMAL(0-10)' \
'      2-DIFICIL(0-15)\033[m')
linhas()
while True:
    tentativas=0
    try:
     escolha=int(input('Qual a escolha [1 ou 2]:'))
    except (ValueError, TypeError):
       print('\033[31mopção invalida, tente novamente\033[m')
       continue
    except KeyboardInterrupt:
       print('\033[31mPROGRAMA INTERROMPIDO PELO USUARIO\033[m')
       break
    if escolha == 1:
       titulos('DIFICULDADE NORMAL')
       computador=randint(0,10)
       while True:
         opçao=int(input('Adivinhe o numero:'))
         tentativas+=1
         if opçao != computador:
          print('\033[31mVOCE ERROU, TENTE NOVAMENTE\033[m')
          if opçao > computador:
                print('DICA:É UM NUMERO MENOR')
          elif opçao < computador:
                print('DICA:É UM NUMERO MAIOR')
          continue
         else:
          print('\033[32mPARABENS!, VOCE ACERTOU\033[m')
          print(f'ACERTOU EM  {tentativas} TENTATIVAS')
          break
    elif escolha == 2:
       titulos('DIFICULDADE DIFICIL')
       computador=randint(0,15)
       while True:
          opçao=int(input('Advinhe o numero:'))
          if opçao != computador:
             print('\033[31mVOCE ERROU, TENTE NOVAMENTE\033[m')
             if opçao > computador:
                print('DICA:É UM NUMERO MENOR')
             elif opçao < computador:
                print('DICA:É UM NUMERO MAIOR')
             continue
          else:
             print('\033[32mPARABENS!, VOCE ACERTOU\033[m')
             print(f'ACERTOU EM {tentativas} TENTATIVAS')
             break
    else:
     print('\033[31mOPÇÃO INVALIDA, TENTE NOVAMENTE\033[m')
     continue
    sair=input('VOCE DESEJA SAIR DO PROGRAMA?[S/N]').upper()
    if sair == 'S':
        print(f'\033[33mSAINDO DO SISTEMA...\033[m')
        sleep(1)
        print('OBRIGADO POR JOGAR')
        break
     
    




