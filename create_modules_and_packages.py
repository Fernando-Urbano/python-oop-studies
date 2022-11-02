"""
Create Modules and Packages
Data: 23/01/2022
"""
def aumentar_preco(valor, pct_aumento):
    return round(valor * (1 + pct_aumento / 100), 2)

def diminuir_preco(valor, pct_aumento):
    return round(valor * (1 - pct_aumento / 100), 2)

# Importar o pacote seria importar "a pasta" que possui todos os arquivos. Podemos fazer isso com
try:
    import package_name.module_name # Importa um modulo
    import package_name
except:
    pass

# Ainda é possível colocar
try:
    from package_name.module_name import function_name
except:
    pass

# É possível ainda criar um subpacote
try:
    import package_name.subpackage_name.mudule_name
except:
    pass

# Todas as exportações não podem estar para trás do arquivo __main__
# O arquivo __main__ é o primeiro arquivo que está sendo executado
# Todos os outros pacotes, modulos, tem que ter commo ponto de referência o __main__
