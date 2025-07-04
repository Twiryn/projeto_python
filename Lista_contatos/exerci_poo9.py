class Agenda_Contatos:
    def __init__(self,nome,telefone,email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
    def __str__(self):
        return f'NOME:{self.nome} ; TEL:{self.telefone} ; EMAIL:{self.email}\n'