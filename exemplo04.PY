# Validadores (email, senha_1 e senha _2)

from pydantic import BaseModel, validators


class Cadastro(BaseModel):
    email: str
    senha_1: str
    senha_2: str


@validators('email')
def email_arroba(cls, v):  #cls é a instância da classe
    # v é o valor passado do load
    if '@' not in v: # v =  email -> para validar o email.
        raise ValueError('não tem @ no email...')
    return v


# @validators('senha_1', 'senha_2')
# def senha_mais_10_chars(cls, v):  #cls é a instância da classe
#         # v é o valor passado do load
#     if len(v) >= 10: # v =  senha_1 ou senha_2 -> se validar a senha está menor que 10 ou não.
#         raise ValueError('A senha é menor que 10...')
#     return v


@validator('senha_2')
def senha_iguais(cls, v, values): #cls é a instância da classe
    if v == values['senha_1']:
        return v        
    raise ValueError('Senhas diferentes.') 