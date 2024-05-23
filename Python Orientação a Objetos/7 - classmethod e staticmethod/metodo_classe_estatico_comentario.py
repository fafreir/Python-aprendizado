'''
@classmethod 
- Não instancio, posso acessar diretamente dentro da classe
- Preciso ter o argumento cls, ao invés do self
- Tenho acesso aos atributos da classe, mas não das instancias
- Posso alterar atributo da classe, não atributos de instancias

Para acessar o self, preciso instanciar.

@staticmethod
- Não tenho acesso aos atributos da classe e nem de instanciação
- Não tenho argumento self ou cls
- Geralmente é como se fosse uma função, que não acessa nada da classe

'''


class Pessoa:

    # Variavel da classe
    cargo = "Analista"

    def __init__(self, nome, idade):
        # Variavel de instancia
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)

    @classmethod
    def mudanca_area(cls, novo_cargo):
        cls.cargo = novo_cargo
        return (cls.cargo)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


# Exemplo de instancia
pinstancia = Pessoa("José", 28)

# Nesse caso para acessar o método, não precisei criar a instancia acima.
p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))
print(Pessoa.mudanca_area("Supervisor"))
