from display import *
from poo import *

while True:
 opçoes()
 try:
    escolha=int(input('Qual sua escolha?'))
    if escolha == 1:
       nome=input('Digite o nome do aluno:')
       email=input('Digite o email do aluno')
       curso=input('Digite o curso do aluno:')
       aluno_novo=Aluno(nome,email,curso)
       session.add(aluno_novo)
       session.commit()
       session.close()
       print('Aluno adicionado com sucesso')
    if escolha == 2:
       busca= session.query(Aluno).all()
       print('='*30)
       print('LISTA DOS ALUNOS CADASTRADOS NO BANCO DE DADOS')
       for i in busca:
        print(i)
       session.close()
       print('='*30)
    if escolha == 3:
      nome=input('Qual será o aluno atualizado:')
      busca=session.query(Aluno).filter_by(nome=nome).first()
      print(busca)
      novo_nome=input('Qual sera o novo nome?')
      novo_email=input('Qual sera o novo email')
      novo_curso=input('Qual sera o novo curso?')
      busca.nome=novo_nome
      busca.email=novo_email
      busca.curso=novo_curso
      session.add(busca)
      print('ALUNO ATUALIZADO')
      menu(busca)
      session.commit()
      session.close()
    elif escolha == 5:
        print('\033[31mFIM DO PROGRAMA\033[m')
        break
 except KeyboardInterrupt:
    print('\033[31mPROGRAMA INTERROMPIPDO PELO USUARIO\033[m')
    break
