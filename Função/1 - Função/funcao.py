'''
FUNÇÃO
- Evita repetição de código

Sintaxe

def nome_da_funcao(argumento_opcional):
    comandos
'''


def dar_boas_vindas():  # sem argumento
    print('Bem vindo')


dar_boas_vindas()


def boas_vindas_personalizada(nome):  # posicional
    print(f'Bem vindo(a) {nome}')


boas_vindas_personalizada('Danielle')


def shoppings(lugar="Vale Sul"):  # nomeada
    print(f'Seu shopping favorito é o {lugar}')


shoppings()
