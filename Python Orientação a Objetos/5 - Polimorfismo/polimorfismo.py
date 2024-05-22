"""

Polimorfismo - utilizar com herança, tenho o mesmo nome de metodo, 
porém com assinaturas diferentes.

"""


class Passaro:
    def voar(self):
        print("Voando...")


class Pardal(Passaro):
    def voar(self):
        super().voar()  # herdando o método da classe pai (Passaro)


class Avestruz(Passaro):
    def voar(self):  # Utilizando meu próprio metodo
        print("Avestruz não pode voar")


def plano_de_voo(passaro):
    passaro.voar()


plano_de_voo(Pardal())
plano_de_voo(Avestruz())
