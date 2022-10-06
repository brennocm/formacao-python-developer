estoque_livraria = {
    "Infanto-juvenil":{"nome": "Percy jackson", "nome": "Harry Potter"},
    "Literatura russa":{"nome": "Guerra e Paz", "nome": "Enfermaria n. 6"},
    "Literatura brasileira":{"nome": "Dom Casmurro", "nome": "A hora da estrela"},
}
estoque_livraria.clear()
print(estoque_livraria)

estoque_livraria = {
    "Infanto-juvenil":{"nome": "Percy jackson", "nome": "Harry Potter"},
    "Literatura russa":{"nome": "Guerra e Paz", "nome": "Enfermaria n. 6"},
    "Literatura brasileira":{"nome": "Dom Casmurro", "nome": "A hora da estrela"},
}
copia = estoque_livraria.copy()
print(copia)

estoque_livraria.fromkeys(["data de lançamento", "Autor"], "vazio")
print(estoque_livraria)

print(estoque_livraria.get("nome"))

print(estoque_livraria.keys())

print(estoque_livraria.pop("Literatura russa"))
print(estoque_livraria.popitem())

print(estoque_livraria.setdefault("autor", "clarisse linspector"))

contatos = {
    "brenno@gmail.com": {"nome": "Brenno", "github": "brennocm"}
}
contatos.update({"ana@gmail.com":{"nome": "Ana", "github": "aninhacode"}})
print(contatos)

print(contatos.values())

verifica = "brenno@gmail.com" in contatos
print(verifica)
verifica2 = "patrick@gmail.com" in contatos
print(verifica2)

del contatos["brenno@gmail.com"]
print(contatos)