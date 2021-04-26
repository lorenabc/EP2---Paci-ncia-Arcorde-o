def empilha(baralho,origem,destino):
    if baralho[origem][-1] == baralho[destino][-1]:
        baralho[destino] = baralho[origem] 
        del baralho[origem]
        return baralho
        
    elif baralho[origem][:-1:] == baralho[destino][:-1:]:
        baralho[destino] = baralho[origem]
        del baralho[origem]
        return baralho

lista = ['A♦', '10♥', 'Q♣', 'K♠', '10♣', '4♠']   
print(empilha(lista,4,1))