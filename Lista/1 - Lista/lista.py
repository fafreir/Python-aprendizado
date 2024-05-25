'''
Em listas, podem podemos ter elementos de vários tipos juntos
Pode ser criado utilizando colchetes[] ou pela palavra reservada list
Tipo de lista é list
Podemos acessar pelo indice
Lembrando que o indice começa por 0
'''

lista = list()
print(type(lista))  # <class 'list'>

preco_1 = 10
preco_2 = 20
preco_3 = 30

# Utilizando colchetes
precos = [10, 20, 30, 40, 50, 60, 100, 250]
print(precos[0])  # acesso é pelo indice
print(precos.index(10))  # 0
print(precos[precos.index(30)])  # 30, acessando pelo index

# Aceitam qualquer tipo de dados
items = [1, 3, 6, 'Ola', 'Café', True, 10.6]
print(items[4])  # Café

# Multiplicação de valores(repetição)
lista_de_noves = [9] * 10
print(lista_de_noves)  # [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]

# Multiplicação, também pode ser com Strings
lista_de_teste = ['Teste'] * 10
# ['Teste', 'Teste', 'Teste', 'Teste', 'Teste', 'Teste', 'Teste', 'Teste', 'Teste', 'Teste']
print(lista_de_teste)

# Usando gerador range(sequencia)
faixa_de_numeros = list(range(30))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
print(faixa_de_numeros)

# Lista de lista(matriz)
matriz_de_nomes = [['Carol', 30], ['Marcus', 50]]
print(matriz_de_nomes[0])  # ['Carol', 30]
print(matriz_de_nomes[0][0])  # Carol
print(matriz_de_nomes[1][0])  # Marcus

# Irá somar todas os valores das listas
lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]
soma = 0
somas = 0

for i in [lista1, lista2]:  # Acessa a lista
    for num in i:  # descompacta/acessa cada valor
        soma += num  # incrementado
        ultimo_valor = num  # recebe o ultimo valor

print(soma)  # 36

# Outra maneira de resolver
for j in lista1 + lista2:
    somas += j

print(somas)  # 36

# Maior numeros em Lista de Lista
matriz = [[42, 23, 34], [100, 215, 114], [10.1, 98.7, 12.3]]
maior = 0

for linha in matriz:
    for num in linha:
        if num > maior:
            maior = num

print(f'Maior numero: {maior}')
