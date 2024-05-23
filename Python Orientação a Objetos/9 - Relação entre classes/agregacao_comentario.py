"""
Agregação
- é um tipo fraco de associação onde uma classe contém referências a instâncias de outra classe, 
- mas a vida dos objetos componentes não depende da vida do objeto agregado.
"""


class Aluno:
    def __init__(self, nome):
        self.nome = nome


class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)


# Criando instâncias
aluno1 = Aluno("Alice")
aluno2 = Aluno("Bob")
curso = Curso("Python")

# Estabelecendo agregação
curso.adicionar_aluno(aluno1)
curso.adicionar_aluno(aluno2)

# Acessando dados
for aluno in curso.alunos:
    print(aluno.nome)  # Saída: Alice, Bob
