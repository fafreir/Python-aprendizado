# Processar VS Retornar
# Return - quando vou precisar reaproveitar em alguma outra lógica

def exibir_cotacao_dia(moeda):
    if moeda == 'usd':
        print(5.47)


def obter_cotacao_do_dia(moeda):
    if moeda == 'usd':
        return 5.47


cotacao = obter_cotacao_do_dia('usd')
if cotacao > 5:
    print("Investir em ações americanas")
else:
    print('Cotação não favorável')
