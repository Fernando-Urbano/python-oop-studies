"""
Unpacking
Data: 26/12/2021


"""
# Transformar lista em variáveis
lista = ['Fernando', 'Ana Luísa', 'Bruno']
primeiro, segundo, terceiro = lista
print(f'1: {primeiro}, 2: {segundo}, 3: {terceiro}')

# Se o número de valores for diferente do tamanho da lista
# é necessário colocar:
lista = ['Fernando', 'Ana Luísa', 'Bruno', 'Joana', 'Bia']
primeiro, segundo, terceiro, *outros = lista
# Cria a lista "outros" com elementos que não foram atribuidos
print(outros)
# Os últimos valores também podem ser alocados
primeiro, *outros, tia = lista
print(outros, tia)
# Caso somente alguns valores forem importantes, o ideal
# é que a lista "*" seja utilizada junto com "_".
# "_" é uma variável não importante