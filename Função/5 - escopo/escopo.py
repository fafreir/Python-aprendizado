"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.

O ESCOPO GLOBAL é o escopo onde todo o código é alcançavel.

O ESCOPO LOCAL é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopo externo

A palavra GLOBAL faz uma variavel do escopo externo
ser a mesma no escopo interno

Cada função tem seu próprio escopo
- Escopo mais interno, consegue acessar o externo
- Tudo que está dentro da função está protegido na função
- Alterar para global dentro da função, não é recomendado
- Se utilizar parametros dentro da função, assim não altera o valor

"""

x = 1
y = 20


def escopo():  # Essa função não consegue acessar valores da função outra_funcao
    # global x  # altero o escopo, com isso a variavel x irá alterar o valor de 1 para 10
    x = 10
    print(f'Na função escopo: x = {x}')

    def outra_funcao():  # Essa função consegue acessar valores da função escopo
        global x
        x = 11
        y = 2  # somente essa função consegue acessar, devido ser local
        print(
            f'Na função outra_funcao: x = {x} e y = {y}')

    def outra_funcao2():
        x = 12  # Irá pegar apenas o valor x local da propria função e do valor global de y
        print(
            f'Na função outra_funcao2: x = {x} e y = {y}')

    outra_funcao()
    outra_funcao2()
    # Cuidado: aqui ainda o escopo é local, porém está como global x = 10
    # Caso a função escopo, x não fosse global, aqui o x não alteraria de valor
    # Mesmo passando por outras funções abaixo, pois não acessa os outros escopos
    print(
        f'Executado dentro da função escopo, depois de passar pelas funções outra_funcao e outra_funcao2: x = {x}')


print(f"Inicialmente o x = {x} e y = {y}")
escopo()  # Acessando a função escopo
# Vai pegar os valores globais, já não está sendo executado dentro da função
# x da função outra_funcao
print(
    f"Depois de passar pelas funções escopo, outra_funcao e outra_funcao2: x = {x} e y = {y}")
