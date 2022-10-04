import sys

saldo = 500.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Saque realizado com sucesso")

else: 
    print("Dinheiro insuficiente para o saque\n")


opcao = int(input("Informe uma opção: \n[1] Sacar \n[2] Extrato:"))
if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
elif opcao == 2:
    print ("Exibindo o extrato...")
else:
    sys.exit("Opção Inválida")


#IF ternário

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")