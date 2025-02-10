
from flask_sqlalchemy import SQLAlchemy

banco_dados = SQLAlchemy()


class Cadastro(banco_dados.Model):
    __tablename__ = 'tb_cadastro'

    id = banco_dados.Column(banco_dados.Integer, primary_key=True)

    nome = banco_dados.Column(banco_dados.String(100))
    idade = banco_dados.Column(banco_dados.Integer)
    cpf = banco_dados.Column(banco_dados.String(100))
    email = banco_dados.Column(banco_dados.String(100))
    endereco = banco_dados.Column(banco_dados.String(100))
    bairro = banco_dados.Column(banco_dados.String(100))
    cep = banco_dados.Column(banco_dados.String(100))

    def __init__(self, nome, idade, cpf, email, endereco, bairro, cep):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        self.endereco = endereco
        self.bairro = bairro
        self.cep = cep

    def to_dict(self):
        return {'nome': self.nome,
                'idade': self.idade,
                'cpf': self.cpf,
                'email': self.email,
                'endereco': self.endereco,
                'bairro': self.bairro,
                'cep': self.cep
                }
