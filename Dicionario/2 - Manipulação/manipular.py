pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 29,
    'empresa': 'Fuentes',

}

# Quantas chaves existem
print(len(pessoa))

# converter em uma lista de tupla
converter_lista = list(pessoa.items())
print(converter_lista)

# converter as keys em lista
converter_lista_chave = list(pessoa.keys())
print(converter_lista_chave)

# converter os values em lista
converter_lista_valor = list(pessoa.values())
print(converter_lista_valor)

# Semelhante ao enumerate
for chave, valor in pessoa.items():
    print(chave, valor)

# Adicionar elemento
# Utilizando o update, não esquecer das chaves, se for dicionario
pessoa.update({'cargo': 'Desenvolvedor'})
print(pessoa)
# Posso também inserir uma tupla com o Update
tupla = (('cidade', 'Atibaia'), ('ano', 1984))
pessoa.update(tupla)
print(pessoa)
# Alterar um valor diretamente
pessoa['cargo'] = 'Engenheiro de Software'
print(pessoa)

# Removendo elemento
# Utilizando pop(chave)
pessoa.pop('cargo')
print(pessoa)
# Utilizando del
del pessoa['empresa']
print(pessoa)

# Remove o ultimo elemento
# Utilizando o popitem
pessoa.popitem()
print(pessoa)
