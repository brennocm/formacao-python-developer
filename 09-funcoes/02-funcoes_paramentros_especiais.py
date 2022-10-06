def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Monza", 1999, "GOK-7841", marca="Chevrolet", motor="2.0", combustivel="Gasolina")

# --

def criar_livro(autor, editora, /, *, nome):
    print(autor, editora, nome)

criar_livro("Vitor Hugo", "Liberté", nome="Os miseráveis")

# --

def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar)

# --

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return print(salario)

salario_bonus(500)
