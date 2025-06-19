def linhas(tam=42):
    print('-'* tam)
def titulos(txt):
    linhas()
    print(txt.center(42))
    linhas()
def Listaclasses():
    print('ESTAS SÃO AS CLASSES DISPONIVEIS:' \
    '\n--CADA CLASSE TEM UM STATUS CORRESPONDENTE--'
          '\n1-GUERREIRO'
          '\n2-MAGO'
          '\n3-ASSASSINO'
          '\n4-TANK'
          '\n\033[31m5-SAIR DO JOGO\033[m')


