# AND = para ser True, tudo precisa ser True
# OR = para ser TRUE, apenas um tem que ser True

print(True and True)
print(True and False)
print(False or False)
print(True or True)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

x = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(f"Comparação sem parenteses: {x}")

y = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(f"Comparação com parenseteses: {y}")