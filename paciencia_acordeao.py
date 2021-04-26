import random

print('Bem vindo(a) ao Paciência Acordeão')
print('\n---------------------------------')
print('\nNesse jogo você pode apenas empilhar:\nUma carta sobre a carta imediantamente anterior \nOu empilhar sobre a terceira carta anterior')
print('\nPara isso acontecer, as cartas, tanto a selecionada quanto a primeira e/ou terceira carta anterior, \nDevem ou ter o mesmo naipe ou mesmo valor!')
print('\nUm pouco complexo, mas você vai pegar o jeito.\n\n')
print('\t\tBom jogo!')

def cria_baralho():
    baralho = ['10♠','5♥','8♦','A♣',
    '9♠','Q♥','10♦','7♣',
    '6♠','6♥','Q♦','8♣',
    'J♠','4♥','4♦','4♣',
    '8♠','8♥','3♦','6♣',
    'A♠','3♥','K♦','10♣',
    '4♠','K♥','J♦','Q♣',
    '3♠','J♥','A♦','5♣',
    'K♠','A♥','6♦','9♣',
    '7♠','2♥','9♦','K♣',
    '5♠','9♥','2♦','2♣',
    '2♠','7♥','5♦','J♣',
    'Q♠','10♥','7♦','3♣']
    
    random.shuffle(baralho)

    return baralho 

print('O baralho inicial está assim:')
baralho_inicial = cria_baralho()
contador = 1
for carta in baralho_inicial:
    print('{}. {}'.format(contador, carta))
    contador += 1