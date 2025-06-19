from tela import cabeçalho
def arquivo_existe(nome):
    try:
        a=open(nome,'rt')
        a.close
    except FileNotFoundError:
        return False
    else:
        return True
def criar_arquivo(nome):
    try:
        a=open(nome,'wt+')
        a.close
    except:
        print('Houve um erro')
    else:
        print(f'Arquivo {nome} criado com sucesso!')
def ler_arquivo(nome):
    try:
        a=open(nome,'rt')
    except:
        print('Houve um erro ao ler o arquivo')
    else:
        print('PESSOAS CADASTRADAS')
        for linha in a:
            dado=linha.split(';')
            dado[1]=dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3}')
    finally:
        a.close()
def adicionar(arq,nome='desconhecido',idade=0):
    try:
        a=open(arq,'at')
    except:
        print('Erro em adicionar uma nova pesso')
    else:
        try:
            a.write(f'{nome} ; {idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado')
