def leia_int(msg):
    while True:
     try:
        n=int(input(msg))
     except(ValueError, TypeError):
        print('\033[31mERRO. Por favor digite um numero valido.\033[m')
        continue
     except(KeyboardInterrupt):
        print('\033[31mEntrada de dados interrompida pelo usuario\033[m')
        return 0
     else:
        return n
def linha(tam=42):
    return '-' * tam
def cabeçalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())
def menu(lista):    
    cabeçalho('MENU')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - {item}')
        c +=1
    opc=leia_int('Sua opção:')
    print(linha())
    return opc
    