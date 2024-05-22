'''
 Modificador de acesso: define o escopo
 Existem 3 modificadores: public, private e protected
 Para modificar para private, _atributo
 Ainda é possível acessar, porém não é uma boa prática
 Uma boa prática, criar um metodo para retornar
'''


class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo  # privado
        self.nro_agencia = nro_agencia  # publico

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo


conta = Conta("0001", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())
