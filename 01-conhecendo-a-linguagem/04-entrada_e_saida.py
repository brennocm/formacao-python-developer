from pyrsistent import b


nome = input("Informe o seu nome: ")
idade = input("informe sua idade: ")

print(f"Meu nome é {nome} e eu tenho {idade} anos")
print(nome, idade, end=" anos\n")
print(nome, idade, sep="#")