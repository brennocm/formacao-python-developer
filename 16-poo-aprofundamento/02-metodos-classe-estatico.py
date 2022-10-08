class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_data_de_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)

p = Pessoa.criar_data_de_nascimento(2003, 3, 20, "Natasha")
print(p.nome, p.idade)