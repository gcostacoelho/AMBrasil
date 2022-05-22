class Denuncia:
    def __init__(self, nomeDenuncia, tel, tipoDesastre, classificacao, situacao):
        self.nome = nomeDenuncia
        self.tel = tel
        self.tipo_desastre = tipoDesastre
        self.classificacao = classificacao
        self.situacao = situacao


class Campanha_Doacao:
    def __init__(self, ong, titulo, descricao, denuncia, meta):
        self.ong = ong
        self.titulo = titulo
        self.descricao = descricao
        self.denuncia = denuncia
        self.meta = meta