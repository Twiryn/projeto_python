import pandas as pd

def Arquivo_Existe():
    try:
        a = open('Contatos.txt','rt')
        a.close
    except FileNotFoundError:
        return False
    else:
        return True
def Criar_arquivo():
    try:
      a=open('Contatos.txt','wt+')
      a.close
    except:
       print('ERRO AO CRIAR ARQUIVO')
    else:
       print('A LISTA DE CONTATOS NAO EXISTE E SERA CRIADA UMA...')
       print('LISTA DE CONTATOS CRIADA COM SUCESSO!')
    
def Adicionar_Contato(pessoa):
    try:
        a = open('Contatos.txt', 'at')
    except:
        print('ERRO AO ADICIONAR CONTATO')
    else:
        try:
            a.write(f'{pessoa}')
        except:
            print('ERRO AO ADICINAR OS DADOS')
        else:
            print(f'CONTATO ADICIONADO COM SUCESSO')
def Listar_contatos():
    try:
     df=pd.read_csv('Contatos.txt',sep=';', header=None,names=['NOME','TEL', 'EMAIL'])
    except FileNotFoundError:
        print('Arquivo nao encontrado')
    else:
        print(df)
def Remover_contatos(excluido):
    try:
     df=pd.read_csv('Contatos.txt',sep=';', header=None,names=['NOME','TEL', 'EMAIL'])
     df_removido=df.drop(index=excluido)
     df_removido.to_csv('Contatos.txt',sep=';', header=False, index=False)
     print('CONTATO REMOVIDO')
    except:
        print('ALGO DEU ERRADO')
