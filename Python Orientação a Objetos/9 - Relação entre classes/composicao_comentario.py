""""
Composição
- É um tipo forte de associação onde uma classe contém instâncias de outra classe.
- A vida dos objetos componentes depende da vida do objeto composto.
"""


class Motor:
    def __init__(self, tipo):
        self.tipo = tipo


class Carro:
    def __init__(self, modelo, tipo_motor):
        self.modelo = modelo
        self.motor = Motor(tipo_motor)


# Criando instância
carro1 = Carro("Toyota", "V8")

# Acessando dados
print(carro1.modelo)  # Saída: Toyota
print(carro1.motor.tipo)  # Saída: V8
