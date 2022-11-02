'''
Try Except with Conditionals
Data: 23/01/2022

'''

# Exemplo
numero = input('Digite um número: ')
print(numero * 5)

# No caso, o python irá entender que o número é na verdade um string
# Para fazer da forma correta

# Correção
# Exemplo
numero = float(input('Digite um número: '))
print(numero * 5)

# Para lidar com usuários que digitam de forma errada:
def converter_numero(valor):
    try:
        return int(valor)
    except ValueError:
        try:
            return float(valor)
        except ValueError:
            pass


numero = None
while numero is None:
    numero = converter_numero(input("Valor: "))

    if numero is None:
        print("Erro: valor digitado não é um número.")



