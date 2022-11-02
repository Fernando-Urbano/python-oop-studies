"""
Expressões em Lambda
Data: 26/12/2021

Funções em lambda são funções anônimas.
Ela é considerada anônima porque não tem nome
"""
# Função comum ----
def multiplication (x, y):
    return x * y

print(multiplication(2, 2))

# Função lambda ----
multiplication = lambda x, y: x * y

print(multiplication(2, 2))

# Exemplo: lista de produtos e seus preços ----
lista_produtos_precos = [
    ["P1", 14],
    ["P2", 10],
    ["P3", 12],
    ["P4", 8],
    ["P5", 19],
    ["P6", 21],
]

# Ordenar pelo preço
def order_price (item):
    return item[1]

lista_produtos_precos.sort(key=order_price, reverse=True)
print(lista_produtos_precos)

# Com a utilização de lambda
lista_produtos_precos = [
    ["P1", 14],
    ["P2", 10],
    ["P3", 12],
    ["P4", 8],
    ["P5", 19],
    ["P6", 21],
]

lista_produtos_precos.sort(key=lambda item: item[1], reverse=True)
print(lista_produtos_precos)

# É utilizada por ser mais fácil e sucinto
