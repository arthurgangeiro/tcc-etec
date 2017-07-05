import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


#class Endereco(Base):
#    __tablename__ = 'endereco'

#    id = Column(Integer, primary_key=True)
#    rua = Column(String(145), nullable=False)
#    numero = Column(Integer, nullable=False)
#    complemento = Column(String(145))
#    bairro = Column(String(145))
#    cidade = Column(String(145))
#    estado = Column(String(145))
#    cep = Column(String(8))
#    pais = Column(String(145))
#    continente = Column(String(145))
#    planeta = Column(String(145))
#    galaxia = Column(String(145))

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
#    endereco_id = Column(Integer, ForeignKey('endereco.id'))
#    endereco = relationship(Endereco)

class Organizacao(Base):
    __tablename__ = 'organizacao'

    id = Column(Integer, primary_key=True)
    cnpj = Column(String(14))
    razaosocial = Column(String(145))
    nomefantasia = Column(String(145))
    representante = Column(String(145))
    email = Column(String(145))
    telefone = Column(String(15))
    endereco = Column(String(255))
#    senha = Column(String(145))
    imagem = Column(String(255))
    descricao = Column(String(999))
    missao = Column(String(145))
    visao = Column(String(145))
    valores = Column(String(145))
#    endereco_id = Column(Integer, ForeignKey('endereco.id'))
#    endereco = relationship(Endereco)    

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

engine = create_engine('sqlite:///projeto.db')


Base.metadata.create_all(engine)