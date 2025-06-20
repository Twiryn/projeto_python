from time import sleep
from dataclasses import dataclass
from tela import *
@dataclass
class personagem:
    nome:str
    hp:int
    ap:int
    atk:int
    def ExibirStatus(personagem):
        print(f'CLASSE: {personagem.nome}'
              f'\nHP:  {personagem.hp}'
              f'\nAP:  {personagem.ap}'
              f'\nATK: {personagem.atk}')
        #CLASSES EXISTENTES
    def classes():
         guerreiro=personagem('GUERREIRO',900,300,35)
         mago=personagem('MAGO',600,800,40)
         assassino=personagem('ASSASSINO',780,530,45)
         tank=personagem('TANK', 1200, 380, 30)
        #MOSTRA OS STATUS DE CADA CLASSE
         while True:    
            print('CARREGANDO...')
            sleep(0.7)
            Listaclasses()
            titulos('\033[33mSELEÇÃO DE CLASSE PARA O JOGADOR\033[m')
            try:
                VerStatus=input('DIGITE O NOME DA CLASSE PARA VER OS STATUS:').strip().upper()
                if VerStatus == 'GUERREIRO':
                    titulos('\033[33m GUERREIRO\033[m')
                    personagem.ExibirStatus(guerreiro)
                elif VerStatus == 'MAGO':
                    titulos('\033[33m MAGO\033[m')
                    personagem.ExibirStatus(mago)
                elif VerStatus == 'ASSASSINO':
                    titulos('\033[33m ASSASSINO\033[m')
                    personagem.ExibirStatus(assassino)
                elif VerStatus == 'TANK':
                    titulos('\033[33m TANK\033[m')
                    personagem.ExibirStatus(tank)
                elif VerStatus == 'SAIR DO JOGO':
                    print('\033[33m SAINDO DO JOGO... \033[m')
                    sleep(1)
                    break
                else:
                 print('\033[31mESTA CLASSE NAO EXISTE, TENTE NOVAMENTE\033[m')
                 continue
                 linhas()
            except(ValueError,TypeError):
               print('\033[31mVALOR INCORRETO, TENTE NOVAMENTE\033[m ')
            except KeyboardInterrupt:
               print('\n\033[31mPROGRAMA INTERROMPIDO PELO USUARIO\033[m')
               break
                #CONFIRMA A SELEÇÃO DE CLASSE
            try:
                SelecionarPersonagem=input('VOCE IRA SELECIONAR ESTE PERSONAGEM?[S/N]').upper() 
                if 'S' != SelecionarPersonagem != 'N':
                    print('\033[31mERRO, SOMENTE [S/N]\033[m')
                elif SelecionarPersonagem == 'S':
                    print(f'\033[33mSELECIONOU A CLASSE {VerStatus}\033[m')
                    print('O JOGO IRA COMEÇAR...')
                    sleep(1.5)
                    break
                elif SelecionarPersonagem == 'N':
                  linhas()
                  continue
            except(ValueError,TypeError):
               print('\033[31mVALOR INCORRETO, TENTE NOVAMENTE\033[m ')
            except KeyboardInterrupt:
               print('\n\033[31mPROGRAMA INTERROMPIDO PELO USUARIO\033[m')
               break
            
