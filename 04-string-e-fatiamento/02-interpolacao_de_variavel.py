nome = "Kratos"
profissao = "Deus da Guerra"
nascimento = "Esparta"

print(f"Meu nome é {nome}! Atualmente, atuo como {profissao} na mitologia Nórdica. Entretanto, sou natural de {nascimento}")

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")

nome = "Brenno"
profissao = "Dev"
linguagem = "Python"

print("Nome: %s profissao: %s linguagem: %s" % (nome, profissao, linguagem))

print("Nome: {} profissão: {}" .format(nome, profissao))

dados = {"nome": "Guilherme", "idade": 28}
print("Nome: {nome} Idade: {idade}" .format(**dados))
