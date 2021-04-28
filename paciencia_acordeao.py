import random
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

def extrai_valor(string):
    return string[:-1:] 

def extrai_naipe(string):
    return string[-1]

def lista_movimentos_possiveis(baralho,indice):
    tamanho  = range(len(baralho))
    posicao1 = (indice-1)
    posicao3 = (indice-3)
    lista = []
    
    if posicao1 in tamanho:
        posicao1_naipe = extrai_naipe(baralho[posicao1])
        posicao1_valor = extrai_valor(baralho[posicao1])

        if posicao1_naipe == extrai_naipe(baralho[indice]) or posicao1_valor == extrai_valor(baralho[indice]):
            lista.append(1)

    if posicao3 in tamanho:
        posicao3_naipe = extrai_naipe(baralho[posicao3])
        posicao3_valor = extrai_valor(baralho[posicao3])

        if posicao3_naipe == extrai_naipe(baralho[indice]) or posicao3_valor == extrai_valor(baralho[indice]):
            lista.append(3)

    return lista

def empilha(baralho,origem,destino):
    destino_naipe = extrai_naipe(baralho[destino])
    destino_valor = extrai_valor(baralho[destino])

    origem_naipe = extrai_naipe(baralho[origem])
    origem_valor = extrai_valor(baralho[origem])

    if origem_naipe == destino_naipe:
        baralho[destino] = baralho[origem] 
        del baralho[origem]
        return baralho        

    elif origem_valor == destino_valor:
        baralho[destino] = baralho[origem]
        del baralho[origem]
        return baralho

def possui_movimentos_possiveis(baralho):
    movimentos = 0
    for contador in range(len(baralho)):
        indicador = lista_movimentos_possiveis(baralho,contador)
        if len(indicador) > 0:
            movimentos += 1

    if movimentos > 0:
        return True
    else:
        return False

print('Bem vindo(a) ao Paciência Acordeão')
print('\n---------------------------------')
print('\nNesse jogo você pode apenas empilhar:\nUma carta sobre a carta imediantamente anterior \nOu empilhar sobre a terceira carta anterior')
print('\nPara isso acontecer, as cartas, tanto a selecionada quanto a primeira e/ou terceira carta anterior, \nDevem ou ter o mesmo naipe ou mesmo valor!')
print('\nUm pouco complexo, mas você vai pegar o jeito.\n\n')
print('\t\tBom jogo!')

jogo = False
iniciar = False
while iniciar != True:
    print('Para iniciar jogo, digite: "Iniciar" ')
    estado = input('')
    if estado == 'Iniciar':
        iniciar = True
        jogo = True

print('O baralho inicial está assim:')
baralho_inicial = cria_baralho()


while jogo:
    contador = 1
    tamanho = range(len(baralho_inicial))
    for carta in baralho_inicial:
        print('{}. {}'.format(contador, carta))
        contador += 1

    contador = 1
    numero = int(input('escolha uma carta: '))
    posicao = (numero-1)
    while posicao not in tamanho:
        numero = int(input('carta invalida. escolha uma carta entre 1 e {}: '.format(max(tamanho)+1)))
        posicao = (numero-1)
    print(posicao)
    print(baralho_inicial[posicao])
    movimento = lista_movimentos_possiveis(baralho_inicial, posicao)
    print(movimento)
    if movimento == [1]:
        print('anterior') 
    elif movimento == [3]:
        print('terceira anterior') 
    elif movimento == [1,3]:
        print('as duas')  
    print('digite "fechar" para encerrar jogo:')
    fechar = input('')
    if fechar == 'fechar':
        jogo = False