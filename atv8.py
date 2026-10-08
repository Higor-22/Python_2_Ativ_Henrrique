#Crie uma lista contendo 3 dicionários. Cada dicionário deve representar um produto,
#contendo as chaves "nome" e "preco". Percorra essa lista com um laço e imprima
#apenas os nomes dos produtos que custam mais de R$ 50,00.

produtos = [
    {"nome": "Produto A", "preco": 30.0}, 
    {"nome": "Produto B", "preco": 60.0}, 
    {"nome": "Produto C", "preco": 40.0}
]

for produto in produtos:
    if produto["preco"] > 50.0:
        print(produto["nome"])