"""
As classes abstratas 
- definem um contrato que as classes derivadas devem seguir.
- As classes que herdarem, precisaram implementar os métodos necessários
- Fornece um módulo ABC, no qual é necessário importar
- Precisa utilizar o decorador @abstractmethod 
"""

# Documentação: https://docs.python.org/pt-br/3/library/abc.html

from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    # @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"


controle = ControleTV()
controle.ligar()
# controle.desligar()
print(controle.marca)


controle = ControleArCondicionado()
controle.ligar()
# controle.desligar()
print(controle.marca)
