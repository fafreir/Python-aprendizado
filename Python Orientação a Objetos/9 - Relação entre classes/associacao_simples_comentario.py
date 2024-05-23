"""
Associação simples 
- é quando uma instância de uma classe contém uma referência a uma instância de outra classe.
"""


class Pessoa:
    def __init__(self, nome):
        self.nome = nome


class Carro:
    def __init__(self, modelo, proprietario):
        self.modelo = modelo
        self.proprietario = proprietario


# Criando instâncias
pessoa1 = Pessoa("Alice")
carro1 = Carro("Toyota", pessoa1)

# Acessando dados
print(carro1.proprietario.nome)  # Saída: Alice
