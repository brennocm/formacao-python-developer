pessoa = {"nome": "Brenno", "idade": 20}
print(pessoa["nome"])

pessoa = dict(nome="Brenno", idade=20)
print(pessoa["idade"])

pessoa["telefone"] = "3222-5855"
print(pessoa["telefone"])

##Dicionários alinhados
jogos_do_ano = {
    "God Of War":{"idade": "+18", "lançamento": "2006"},
    "FIFA":{"idade": "Livre", "lançamento": "2004"},
    "GTA":{"idade": "+18", "lançamento": "2008"}
}

print(jogos_do_ano["God Of War"])