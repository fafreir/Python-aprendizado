class Bicicleta:
    numero_de_rodas = 2

    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro

    def buzinar(self):
        print('Plimmmmmmmmm')

    def parar(self):
        print('Parando bicicleta ... ')
        print('Bicicleta parada!')

    def correr(self):
        print('Vrummmm')

    def get_cor(self):
        return self.cor

    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta('vermelho', 'caloi', 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.get_cor())
b1.cor = "azul"
print(b1.cor)
del b1.cor
print(b1.numero_de_rodas)
print(b1)
