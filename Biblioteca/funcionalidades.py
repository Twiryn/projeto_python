from BancoDeDados import *
def titulos(txt):
    print('#'*30)
    print(txt.center(30))
    print('#'*30)
def opc():
    print('1-Adicionar Usuario',
          '\n2-Adiconar Livro',
          '\n3-Listar Usuarios',
          '\n4-Listar Livros')
def Add_Usuario():
    nome=input('NOME:')
    email=input('EMAIL:')
    pessoa=Usuario(nome,email)
    try:
        session.add(pessoa) 
        session.commit()
        session.close()
    except:
        print('ERRO!')
    else:
        print('USUARIO ADICIONADO COM SUCESSO')
def Add_Livro():
    try:
        nome_lv=input('NOME DO LIVRO:')
        qtde=int(input('QTDE DE PAG:'))
        autor=input('AUTOR DO LIVRO:')
        novo_livro=Livro(nome_lv,qtde,autor)
        session.add(novo_livro)
        session.commit()
        session.close()
    except:
       pass
    else:
        print('LIVRO ADICIONADO COM SUCESSO')