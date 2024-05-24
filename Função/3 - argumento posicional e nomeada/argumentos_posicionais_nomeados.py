def exibir_preco(nome_produto, preco):  # Argumento posicional
    print(f'{nome_produto} esta no valor de: {preco}')


# Argumento posicional
exibir_preco(5000, 'Iphone')

# Argumento nomeado
# Independe da ordem colocada
exibir_preco(nome_produto='Iphone', preco=5000)
exibir_preco(preco=5000, nome_produto='Iphone')

# Para forçar argumento nomeado
# Precisa utilizar o *, tudo que vier depois precisará ser nomeado
# Se não colocar o argumento nomeado, apresentará erro


def exibir_produto(nome, *, quantidade):
    print(f'{nome} e quantidade {quantidade}')


exibir_produto('Banana', quantidade=3)
exibir_produto(quantidade=3, nome='Banana')
