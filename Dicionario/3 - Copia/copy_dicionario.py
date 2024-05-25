# copy - retorna uma cópia rasa (shallow copy)
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

# CUIDADO:
# Irá apontar para o mesmo endereço de memória que d1
# Porém se alterar em d2, irá alterar também em d1
# d2 = d1

# SHALLOW COPY
# .copy - irá criar um novo dicionario
# Com isso os valores imutáveis irão se alterar
# Para valores mutaveis, irá apontar para o mesmo endereço de memória
d2 = d1.copy()

# SHALLOW COPY
# CUIDADO
# Como listas apontam para o mesmo endereço de memória
# Ao alterar de uma das listas,
# irá se propagar para as outras que estão na mesmo endereço
# Serve para dados imutaveis (int, str, float, dicionario, tupla ...)
d2['c1'] = 1000  # dicionario(imutavel)
d2['l1'][1] = 999999  # lista (mutavel)
print(d1)
print(d2)

print()
# DEEP COPY
# Necessário importar o copy
# Copia profunda, irá alterar somente na que foi alterada
# Serve para valores mutaveis
d2 = copy.deepcopy(d1)
d2['c1'] = 1  # Dado Imutavel
d2['l1'][1] = 2  # Dado Mutavel

print(d1)
print(d2)
