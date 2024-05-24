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


def escopo():  # Essa função não consegue acessar valores da função outra_funcao
    global x  # altero o escopo, com isso a variavel x irá alterar o valor
    x = 10

    def outra_funcao():  # Essa função consegue acessar valores da função escopo
        global x
        x = 11
        y = 2  # somente essa função consegue acessar, devido ser local
        print(x, y)

    outra_funcao()
    print(x)


print(x)  # 1
escopo()  # 11 2 11
print(x)  # 11
