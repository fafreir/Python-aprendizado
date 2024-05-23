"""
Associação bidirecional
- ambas as classes contêm referências uma à outra
"""


class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.carro = None


class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.proprietario = None


# Criando instâncias
pessoa1 = Pessoa("Alice")
carro1 = Carro("Toyota")

# Estabelecendo associação bidirecional
pessoa1.carro = carro1
carro1.proprietario = pessoa1

# Acessando dados
print(pessoa1.carro.modelo)  # Saída: Toyota
print(carro1.proprietario.nome)  # Saída: Alice
