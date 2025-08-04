from sqlalchemy import create_engine, Column, String, Integer, Boolean,ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
#criação do banco de dados e a sessao
db=create_engine("sqlite:///meubanco.db")
Session=sessionmaker(bind=db)
session=Session()
 
Base=declarative_base()
# As tabelas
class Usuario(Base):
    __tablename__ = "Usuarios"
    id = Column("id", Integer, primary_key=True, autoincrement=True) 
    nome=Column("Nome", String)
    email= Column("Email", String)
    ativo=Column("Ativo", Boolean)
    def __init__(self, nome, email, ativo=True):
        self.nome=nome
        self.email=email
        self.ativo=ativo

class Livro(Base):
    __tablename__ = "Livros"
    id = Column("id", Integer,primary_key=True, autoincrement=True)
    titulo=Column("Titulo", String)
    qtde_paginas=Column("Qtde_paginas",Integer)
    autor=Column("Autor",String)
    def __init__(self, titulo, qtde_paginas,autor):
        self.titulo = titulo
        self.qtde_paginas = qtde_paginas
        self.autor=autor
Base.metadata.create_all(bind=db)
