class Tipo_Desastre:
    def __init__(self, descricao):
        self.descricao = descricao

class Tipo_Local:
    def __init__(self, siglaEstado, cidade, logradouro, cep):
        self.sigla_estado = siglaEstado
        self.cidade = cidade
        self.logradouro = logradouro
        self.cep = cep

class Classificacao:
    def __init__(self, descricao):
        self.descricao = descricao
