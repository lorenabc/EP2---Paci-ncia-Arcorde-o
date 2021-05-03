import random
def cria_baralho():
    baralho = ['K♠', 'Q♠', 'J♠', '10♠', 
    '9♠', '8♠', '7♠', '6♠', 
    '5♠', '4♠', '3♠', '2♠', 
    'A♠', 'K♥', 'Q♥', 'J♥', 
    '10♥', '9♥', '8♥', '7♥',
    '6♥', '5♥', '4♥', '3♥', 
    '2♥', 'A♥', 'K♦', 'Q♦', 
    'J♦', '10♦', '9♦', '8♦',
    '7♦', '6♦', '5♦', '4♦', 
    '3♦', '2♦', 'A♦', 'K♣', 
    'Q♣', 'J♣', '10♣', '9♣',
    '8♣', '7♣', '6♣', '5♣', 
    '4♣', '3♣', '2♣', 'A♣']

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
print('\t\tBom jogo!\n')

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
    numero = int(input('\nEscolha uma carta entre 1 e {}: '.format(max(tamanho)+1)))
    posicao = (numero-1)
    posicao1 = (posicao-1)
    posicao3 = (posicao-3)
    
    while posicao not in tamanho:
        numero = int(input('Carta invalida. Escolha uma carta entre 1 e {}: '.format(max(tamanho)+1)))
        posicao = (numero-1)

    movimento = lista_movimentos_possiveis(baralho_inicial, posicao)

    if movimento == []:
        print('Não há movimentos possíveis para a carta {}.\n'.format(baralho_inicial[posicao]))

    elif movimento == [1]:
        empilha(baralho_inicial, posicao, posicao1)

    elif movimento == [3]:
        empilha(baralho_inicial, posicao, posicao3) 

    elif movimento == [1,3]:
        print('Quer empilhar {} sobre qual carta?'.format(baralho_inicial[posicao]))
        print('\n 1. {}'.format(baralho_inicial[posicao1]))
        print(' 2. {}'.format(baralho_inicial[posicao3]))
        escolha = int(input(''))
        if escolha == 1:
            empilha(baralho_inicial, posicao, posicao1)
        elif escolha == 2:
            empilha(baralho_inicial, posicao, posicao3)
        
    print('digite "fechar" para encerrar jogo:')
    fechar = input('')
    if fechar == 'fechar':
        jogo = False
        
    elif fechar != 'fechar':
        jogo = True
        print('\nO baralho está assim:')

    # verificacao = possui_movimentos_possiveis(baralho_inicial)
    # if verificacao != True:
    #     jogo = False

print('Não há mais movimentos possíveis.')
print('Você perdeu!')