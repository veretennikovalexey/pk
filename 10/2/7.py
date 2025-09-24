import random

# seed = int(input())
seed = 87
random.seed(seed)

# список мастей карт
масти = ['♠', '♣', '♥', '♦']

# список номиналов карт
номиналы = ['6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т']

# колода 36 карт ( масть + достоинство )
deck = [масть + номинал for масть in масти for номинал in номиналы]

# перемешиваем колоду
random.shuffle(deck)

# раздаём первому игроку 6 карт deck[0:6]
first_player = deck[0:6]
second_player = deck[6:12]

print(f'Игрок 1: {", ".join(first_player)}')
print(f'Игрок 2: {", ".join(second_player)}')

'''
Sample Input:

87
Sample Output:

Игрок 1: ♦Т, ♣10, ♠К, ♣В, ♥К, ♠В
Игрок 2: ♦10, ♥6, ♦6, ♥В, ♠10, ♠7
'''