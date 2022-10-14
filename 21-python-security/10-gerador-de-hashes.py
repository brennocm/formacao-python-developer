import hashlib

string = input("Digite o texto a ser transformado em hash: ")
menu = int(input('''                     --> Menu <--
                 # Escolha o tipo de hash #
                 # 1) MD5
                 # 2) SHA1
                 # 2) SHA256
                 # 3) SHA512
                 Digite o número do hash a ser gerado: '''))

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print("O hash MD5 de", string, "é: ", resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print("O hash SHA1 de", string, "é: ", resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print("O hash SHA256 de", string, "é: ", resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print("O hash SHA512 de", string, "é: ", resultado.hexdigest())
else:
    print("Algo não deu certo, tente novamente!")