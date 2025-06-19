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
         assasino=personagem('ASSASSINO',780,530,45)
         tank=personagem('TANK', 1200, 380, 30)
        #MOSTRA OS STATUS DE CADA CLASSE
         while True:    
            print('CARREGANDO...')
            sleep(0.7)
            Listaclasses()
            titulos('\033[33mSELEÇÃO DE CLASSE PARA O JOGADOR\033[m')
            try:
                VerStatus=int(input('DIGITE O NUMERO DA CLASSE PARA VER OS STATUS:')) 
                if VerStatus == 1:
                    titulos('\033[33m GUERREIRO\033[m')
                    personagem.ExibirStatus()
                elif VerStatus == 2:
                    titulos('\033[33m MAGO\033[m')
                    personagem.ExibirStatus(mago)
                elif VerStatus == 3:
                    titulos('\033[33m ASSASSINO\033[m')
                    personagem.ExibirStatus(assasino)
                elif VerStatus == 4:
                    titulos('\033[33m TANK\033[m')
                    personagem.ExibirStatus(tank)
                else:
                 print('\033[31mESTA CLASSE NAO EXISTE, TENTE NOVAMENTE\033[m')
                 linhas()
                 continue
                #CONFIRMA A SELEÇÃO DE CLASSE
                while True:
                 SelecionarPersonagem=input('VOCE IRA SELECIONAR ESTE PERSONAGEM?[S/N]').upper() 
                 if SelecionarPersonagem == 'N':
                  linhas()
                  break
            except(ValueError,TypeError):
               print('\033[31mVALOR INCORRETO, TENTE NOVAMENTE\033[m ')
            except KeyboardInterrupt:
               print('\n\033[31mPROGRAMA INTERROMPIDO PELO USUARIO\033[m')
               break
            