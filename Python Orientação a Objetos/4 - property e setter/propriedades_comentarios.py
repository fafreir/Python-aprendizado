'''

Geralmente o getter e o setter, são utilizados, quando o atributo é privado.

@property - irá retornar, em outras linguagem equivale ao get.

@atributo.setter - para realizar modificações, não retorna valor.

@atributo.setter - permite remover um atributo.

'''


class Foo:
    def __init__(self, x=None):
        self._x = x

    # getter
    @property
    def x(self):
        return self._x or 0

    # setter
    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0


class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def idade(self):
        ano_atual = 2024
        return ano_atual - self._ano_nascimento


foo = Foo(10)
print(foo.x)
foo.x = 15
print(foo.x)
del foo.x
print(foo.x)

pessoa = Pessoa("Fabrício", 1989)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
