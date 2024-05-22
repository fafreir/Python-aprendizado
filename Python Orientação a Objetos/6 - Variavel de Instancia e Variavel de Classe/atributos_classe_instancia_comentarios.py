class Estudante:
    # variavel de classe
    escola = "DIO"

    def __init__(self, nome, matricula):
        # variavel da instancia
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


# Variavel da instancia, altera somente para a instancia (copia)
aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)
mostrar_valores(aluno_1, aluno_2)

# Alterado o aluno_1
aluno_1.matricula = 3
mostrar_valores(aluno_1, aluno_2)

# Variavel de classe, altera para todos (unico objeto), utilizando a classe
Estudante.escola = "Python"
# Irá alterar apenas a matricula do aluno_1
aluno_1.matricula = 10
mostrar_valores(aluno_1, aluno_2)

# Não irá alterar o nome
Estudante.nome = "Java"

# Irá alterar o nome da escola do aluno_2
aluno_2.escola = "C++"

# Irá criar o objeto/instanciação aluno_3
aluno_3 = Estudante("Charlie", 5)
mostrar_valores(aluno_1, aluno_2, aluno_3)
