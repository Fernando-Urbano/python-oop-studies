'''
Count - Itertools
Data: 20/01/2022

'''
variavel = zip('Alo', 'Alo')
print(next(variavel))
print(next(variavel))
print(next(variavel))

# Alo é um iterável
# Zip é um iterador
# Portanto, "variavel" é um iterador

print("#" * 20)

variavel = ((x, y) for x, y in zip("Alo", "Alo"))
print(next(variavel))
print(next(variavel))
print(next(variavel))

# Cuidado com loopings infinitos
# count() pode gerar loopings infinitos por ser um iterador infinito
from itertools import count

contador = count(start=-1e2, step=2.5)
# Se o step for um número negativo, ele irá contar do maior para o menor

for valor in contador:
    print(round(valor, 3))

    if abs(valor) == 1e2:
        break  # Caso contrário seria infinito

# Outro exemplo com contador
contador = count(start=1e6)
nomes = ['Luiz', 'Bia', 'Bruno']
nomes = zip(contador, nomes)
print(list(nomes))