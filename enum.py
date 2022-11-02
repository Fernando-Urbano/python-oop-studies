"""
Enum
Data: 06/02/2022

É um tipo de dado. Isso somente foi adicionado na versão 3.4 do python

"""
from enum import Enum, auto


# Supomos um jogo em que temos que mover o jogador
def move(direction):
    if direction != 'right' and direction != 'left':
        raise ValueError(f'Cannot move in this direction.')

    return f'Moving {direction}'


if __name__ == "__main__":
    print(move('right'))
    print(move('left'))
    # print(move('up'))
    # print(move('down'))


# Toda a vez que adiciono uma nova possibilidade, tenho que adicioná-la em cima também
# Para conseguir fazer isso de forma mais simples:


class Directions(Enum):
    right = 0
    left = 1


def move(direction):
    if not isinstance(direction, Directions):
        raise ValueError(f'Cannot move in this direction.')

    return f'Moving {direction.name}'


if __name__ == "__main__":
    print(move(Directions.right))
    print(move(Directions.left))


# Outra forma de definir o enum é colocando auto():

class Directions(Enum):
    right = auto()
    left = auto()
    up = auto()
    down = auto()


if __name__ == "__main__":
    print(move(Directions.up))
    print(move(Directions.left))
    print(move(Directions.down))
    try:
        print(move('front'))
    except ValueError as error:
        print(error)