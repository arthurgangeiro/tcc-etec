__author__ = "Arthur Grangeiro de Souza"
__credits__ = ["Arthur Grangeiro de Souza"]
__version__ = "0.9.1"
__maintainer__ = "Arthur Grangeiro de Souza"
__email__ = "arthurgrangeiro@outlook.com"
__status__ = "Prototype"


import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'  

    id = Column(Integer, primary_key=True)
    email= Column(String(145))
    senha = Column(String(145))
    telefone = Column(String(15))
    endereco = Column(String(255))
    nome = Column(String(145))
    cpf = Column(String(11))
    nascimento = Column(String(10))
    genero = Column(String(2))

class Organizacao(Base):
    __tablename__ = 'organizacao'

    id = Column(Integer, primary_key=True)
    ativo = Column(String(20))
    cnpj = Column(String(20))
    razaosocial = Column(String(145))
    nomefantasia = Column(String(145))
    representante = Column(String(145))
    email = Column(String(145))
    telefone = Column(String(15))
    endereco = Column(String(255))
    site = Column(String(255))
    facebook = Column(String(255))
    doacao = Column(String(255))
    logo = Column(String(255))
    imagem = Column(String(255))
    sobre = Column(String(145))
    descricao = Column(String(999))


class Cartao(Base):
    __tablename__ = 'cartao'

    id = Column(Integer, primary_key=True)
    numero = Column(String(16), nullable=False)
    nome = Column(String(145), nullable=False)
    validade = Column(String(10), nullable=False)
    cpf = Column(String(11), nullable=False)
    cvv = Column(String(3), nullable=False)
    user_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship(Usuario)


class DadosBancarios(Base):
    __tablename__ = 'dados_bancarios'

    id = Column(Integer, primary_key=True)
    banco = Column(String(145), nullable=False)
    agencia = Column(String(15), nullable=False)
    conta = Column(String(15), nullable=False)
    tipo = Column(String(2), nullable=False)
    org_id = Column(Integer, ForeignKey('organizacao.id'))
    organizacao = relationship(Organizacao)

class Mensagem(Base):
    __tablename__ = 'mensagens'

    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    message = Column(String(999), nullable=False)


engine = create_engine('sqlite:///projeto.db')

Base.metadata.create_all(engine)