'''
Decorator
- Posso alterar o comportamento da função
- Preciso da anotação @nome_funcao
- Dentro da função que está como decorator, vou conseguir acessar as informações da outra função
- É como se eu entrasse na função que está como decorator, e passasse a outra função como argumento
'''
from datetime import datetime


def depositar_dinheiro():
    print('depositando dinheiro')

    def depositando_dolar():
        print('Depositando dolares')

    def depositando_reais():
        print('Depositando reais')

    # depositando_dolar()
    depositando_reais()


depositar_dinheiro()


def pai(numero):
    def filho_1():
        print('Sou filho 1')

    def filho_2():
        print('Sou filho 2')
    if numero == 1:
        return filho_1
    elif numero == 2:
        return filho_2


resultado = pai(1)
resultado()


# Decorators
def meu_decorator(funcao):
    print("Entrei no escopo meu_decorator")

    def wrapper():
        print('Antes')
        funcao()
        print('Depois')
    return wrapper


@meu_decorator
def parabenizar():
    print('Parabéns!!!')


# resultado = meu_decorator(parabenizar)
# resultado()
parabenizar()
