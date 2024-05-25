valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
anos = [2020, 2030, 2040, 2050]

# Adiciona no final da lista
valores.append(11)
print(valores)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 11]

# Unir listas
valores.extend(anos)
print(valores)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 11, 2020, 2030, 2040, 2050]

# Adiciona lista
nova_lista = valores + anos
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 11, 2020, 2030, 2040, 2050, 2020, 2030, 2040, 2050]
print(nova_lista)

# Inserir (posição, valor)
anos.insert(2, 2031)
print(anos)  # [2020, 2030, 2031, 2040, 2050]

# Extrair/remover com base no indice ou valor, e retorna o valor removido
anos_2020 = anos.pop(0)
print(anos)  # [2030, 2031, 2040, 2050]

# Remove - remove apenas pelo valor e não retorna o valor removido
# anos.remove(2050)
del anos[3]  # posso remover por faixas [2:5]
print(anos)  # [2030, 2031, 2040]

del valores[1:7]  # indice [inicial:final]
print(valores)  # [1, 8, 9, 100, 11, 2020, 2030, 2040, 2050]

# contando a ocorrencia de um valor
print(valores.count(8))  # 1

# Resetar (apagar todos)
# valores.clear()

# Ordenar em ordem crescente
valor = [31, 23, 6, 36, 21, 33, 7, 20, 23]
valor.sort()  # não modifica, apenas irá ordenar
print(valor)  # [6, 7, 20, 21, 23, 23, 31, 33, 36]

# Ordenar em ordem descrente
valor.sort(reverse=True)
print(valor)  # [36, 33, 31, 23, 23, 21, 20, 7, 6]

# Inverter uma lista
valor.reverse()
print(valor)  # [6, 7, 20, 21, 23, 23, 31, 33, 36]
