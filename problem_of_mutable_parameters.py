"""
Problem of Mutable Parameters in Functions
Data: 24/01/2022

"""
def lista_clientes(clientes_iteravel, lista=[]):
    #  Ideia de colocar a lista atual no parametro "lista"
    lista.extend(clientes_iteravel)
    return lista

primeira_lista = lista_clientes(['João', 'Maria', 'Eduardo'])
segunda_lista = lista_clientes(['Marcos', 'Jonas', 'Zico'])

# As listas que deveriam estar separadas na verdade estão unidas
print(primeira_lista)
print(segunda_lista)

# O problema está em ter um objeto mutável
# Por exemplo, listas, dicionários, etc...

# O parametro "lista", uma vez "setado" adiciona novos valores todas as vezes que é chamado
# Como podemos solucionar o problema?

def lista_clientes(clientes_iteravel, lista=None):
    if lista == None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista

primeira_lista = lista_clientes(['João', 'Maria', 'Eduardo'])
segunda_lista = lista_clientes(['Marcos', 'Jonas', 'Zico'])

print(primeira_lista)
print(segunda_lista)

# Agora funcionou!
# Cuidado com objetos mutáveis