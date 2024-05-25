# dicionario_pessoa = dict(nome='Carol', idade=18, altura=1.60)
dicionario_pessoa = {'nome': 'Carol', 'idade': 18, 'altura': 1.60}

# Imprimir somente o valor de idade
# nome_dicionario['key']
print(dicionario_pessoa['idade'])  # 18

# Imprimir somente as chaves
# Pode utilizar a palavra reservada keys
# nome_dicionario.keys()
print(dicionario_pessoa.keys())  # dict_keys(['nome', 'idade', 'altura'])
# Posso acessar por iteração
for chave in dicionario_pessoa.keys():
    print(chave)

# Imprimir somente os valores
# Pode utilizar a palavra reservada values
# nome_dicionario.values()
print(dicionario_pessoa.values())  # dict_values(['Carol', 18, 1.6])
# Posso acessar por iteração
for valor in dicionario_pessoa.values():
    print(valor)

# Imprimir chaves e valores
# Pode utilizar a palavra reservada items
# nome_dicionario.items()
# dict_items([('nome', 'Carol'), ('idade', 18), ('altura', 1.6)])
print(dicionario_pessoa.items())


# Iterar sobre o dicionario - [0] acessa keys - [1] os values
for item in dicionario_pessoa.items():
    print(item)  # mostra a tupla
    print(item[0])  # mostra as chaves
    print(item[1])  # mostra os valores

# Utilizando o get, posso acessar o valor
# nome_dicionario.get('nome_chave')
# Por padrão, devolve None ou alguma mensagem
# Posso colocar alguma mensagem caso não exista
# nome_dicionario.get('nome_chave',  'mensagem' )
print(dicionario_pessoa.get('nome'))
print(dicionario_pessoa.get('cargo', 'chave cargo não existe'))
# Quando a chave não existe, posso também utilizar setdefault
print(dicionario_pessoa.setdefault('cargo', 'chave cargo não existe'))
