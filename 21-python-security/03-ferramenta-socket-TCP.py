import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET,  socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou!!!")
        print("Erro: {}". format(e))
        sys.exit()

    print("Socket criado com sucesso!")

    hostAlvo = input("Digite o Host ou IP aa ser conecado:")
    portAlvo = input("Digite a porta a ser conectada:")

    try:
        s.connect((hostAlvo, int(portAlvo)))
        print("Cliente TCP conectado com sucesso no host: " + hostAlvo + " e na Porta: " + portAlvo)
    except socket.error as e:
        print("Não foi possível conectar no host: " + hostAlvo + " e na porta: " + portAlvo)
        print("Erro: {}".format(e))
        sys.exit

if __name__ == "__main__":
    main()