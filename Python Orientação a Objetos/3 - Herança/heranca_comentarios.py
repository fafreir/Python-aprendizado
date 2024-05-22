'''
 Na herança é herdado: atributos e métodos da classe pai

 classe pai ou base - a classe de onde os atributos e métodos são herdados
 
 classe filha - é a que herda
'''


class Veiculo:  # classe pai ou base
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):  # classe filha
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    # Todos atributos, tanto herdado quanto da classe
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)  # Atributos herdados
        self.carregado = carregado  # atributo da classe Caminhao

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado.")


moto = Motocicleta("preta", "abc-1234", 2)
print(moto)
moto.ligar_motor()

caminhao = Caminhao("roxo", "gfd-8712", 8, True)
print(caminhao)
caminhao.esta_carregado()
