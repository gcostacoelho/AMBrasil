class Usuario:
    def __init__(self, nome, email, cpf) -> None:
        self.nome = nome
        self.email = email
        self.cpf = cpf

class Ong:
    def __init__(self, nome, cnpj, endereco, email, telefone, bio):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.email = email
        self.tel = telefone
        self.bio = bio
