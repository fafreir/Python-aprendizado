# *args - posso ter inumeros argumentos, no qual são tuplas.
# Porem o b, precisará ser nomeado quando chamado
def somar(*valores):
    b = 0
    for valor in valores:
        b += valor
    print(b)

somar(10, 20, 5)

# **kwargs(cs)
# Posso ter inumeros argumentos, porém nomeados, no qual são dicionários
def concatenar(**palavras):
    frase = ''
    for palavra in palavras.values():
        frase += palavra + ' '
    print(frase)


concatenar(a='Nós', b='somos', c='todos', d='Pythonistas', e='Profissionais')


def fazer_calculo(nome, *args, **kwargs):
    print(nome)
    # print(args)
    # print(kwargs)
    for arg in args:
        print(arg)
    for kw in kwargs.keys():
        print(kw)
    for kwargs in kwargs.values():
        print(kwargs)


fazer_calculo('Jeff', 4, 6, 3, 7, a=1, b=2, c=3)
