"""
Cuidados com dados mutáveis
- copiado o valor (imutáveis)
- aponta para o mesmo valor na memória (mutável)
- copy, realiza uma copia rasa, aponta para o mesmo espaço de memória
- deepcopy, realiza uma copia profunda, necessário importar o deepcopy

"""
from copy import deepcopy

lista_a = [1, 3, 5]
# lista_b = lista_a.copy()  # copia rasa
lista_b = deepcopy(lista_a)  # copia profunda

lista_b[0] = 3
print(lista_a)
print(lista_b)
