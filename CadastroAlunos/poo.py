from sqlalchemy import create_engine,Column, String ,Integer
from sqlalchemy.orm import sessionmaker, declarative_base
db=create_engine("sqlite:///BandoDeDados.db")
Session=sessionmaker(bind=db)
session=Session()

Base=declarative_base()
class Aluno(Base):
    __tablename__='Alunos'
    id=Column('Id',Integer, primary_key=True ,autoincrement=True)
    nome=Column('Nome',String)
    email=Column('Email',String)
    curso=Column('Curso',String)
    def __init__(self, nome, email,curso):
        self.nome=nome
        self.email=email
        self.curso=curso
    def __repr__(self):
        return f"Nome:{self.nome}\nEmail:{self.email}\nCurso:{self.curso}\n"
Base.metadata.create_all(bind=db)
