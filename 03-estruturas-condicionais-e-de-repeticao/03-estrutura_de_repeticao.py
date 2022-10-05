nome_livro = input("Informe o nome do livro: ")
VOGAIS = "AEIOU"

#for with iteration
for letra in nome_livro:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()

#for with range
for numero in range(0, 31, 3):
    print(numero)
else:
    print()

#while
opcao = 0

while opcao == 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[3] Sair\n"))
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Imprimindo extrato...")
else:
    print()

