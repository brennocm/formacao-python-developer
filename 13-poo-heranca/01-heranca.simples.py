class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print("Ligando motor")

    def __str__(self):
        return self.cor

class Motococileta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        self.carregado = carregado

        super().__init__(cor, placa, numero_rodas)

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto = Motococileta("Preto", "GOK-222", 2)
moto.ligar_motor()

carro = Carro("Cinza", "GOK-232", 4)
carro.ligar_motor()
