# Permite combinar elementos de duas ou mais listas em uma unica lista

from itertools import zip_longest

# Multiplas listas - zip (mesmo tamanho ambos)
produtos = ['produto 1', 'produto 2', 'produto 3', 'produto 4', 'produto 5']
precos = [250, 150, 220, 550, 50]

for a, b in zip(produtos, precos):
    print(f'Salvando produto {a} valor R$ {b}')

# Multiplas listas - zip_longest (não simetrico)
titulos = ['Titulo 1', 'Titulo 2', 'Titulo 3', 'Titulo 4']
descricoes = ['Descricao 1', 'Descricao 2', 'Descricao 3']
for titulo, descricao in zip_longest(titulos, descricoes):
    print(f'Encontramos o {titulo} descrição: {descricao}')
