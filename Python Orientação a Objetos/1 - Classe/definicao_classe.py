# As classes definem atributos e comportamentos que caracterizam os objetos,
# enquanto os objetos são instâncias das classes.

# O nome da classe, segue convenção CamelCase
class Bicicleta:
    # Variavel da classe, todos teriam o mesmo numero de rodas
    numero_de_rodas = 2

    # Construtor ou Método Construtor
    def __init__(self, cor, modelo, ano, valor, aro=18):
        # self- refere ao objeto atual (explicito),porém poderia ser outro nome
        # self, usado para acessar variaveis que pertencem a classe
        # atributos - inicializar os atributos
        # atributos, são como variaveis que pertencem a instancia de uma classe
        # Variaveis de instância
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro

    # método
    # não confundir com função, e nem esquecer do self
    # Podem acessar e modificar atributos, até executar alguma ação
    # Definem comportamentos para os objetos da classe
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
    '''
    def __str__(self):
        return f'{self.__class__.__name__}: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}'
    '''


# Criando objeto
# Chama pelo nome da classe, como se fosse uma função
b1 = Bicicleta('vermelho', 'caloi', 2022, 600)

# Posso acessar um método via ponto
b1.buzinar()  # Bicicleta.buzinar(b1)
b1.correr()
b1.parar()
print(b1.get_cor())

b1.cor = "azul"  # Alterar um valor

# Posso acessar também um atributo com o ponto
print(b1.cor)
del b1.cor  # deletar
print(b1.numero_de_rodas)
print(b1)
