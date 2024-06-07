import json

produtos = {
    'ps5': {

        'id': 2022,
        'valor': 5000,
        'quantidades': 100},
    'god of war ragnarock': {
        'id': 2023,
        'valor': 250,
        'quantidade': 50}}

with open('produtos.json', 'w') as meu_arquivo:
    json.dump(produtos, meu_arquivo)

with open('produtos.json', 'r') as arquivo:
    print(json.load(arquivo))
