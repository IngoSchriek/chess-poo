from Classes_Xadrez import Peça, Tabuleiro
from utils import verifica_peça_no_tabuleiro,modifica_turno,check

import numpy as np

turno=0

tab = Tabuleiro()
P1 = Peça([4, 4], 'P1', tab)
p1 = Peça([3, 4], 'p1', tab)
mapeamento_peças = {'P1': P1, 'p1': p1}

print(tab.get_estado())


while True:
    #pede a peça desejada e já deixa no do time tlgd
    
    peça_desejada = modifica_turno(turno,input('Peça: '))
    peça_desejada = verifica_peça_no_tabuleiro(mapeamento_peças, peça_desejada)

    peça_movendo = mapeamento_peças[peça_desejada]
    pos_atual = peça_movendo.get_posi()
    pos_desejada = list(map(int,input('Digite a posição desejada, para selecionar outra peça, digite -1: ').split()))
    if pos_desejada[0] == -1:
        #recomeça o loop
        continue
    rei_turno=modifica_turno(turno,"R")
    if peça_desejada!=rei_turno:
        check=check(rei_turno,mapeamento_peças)
    else:
        check=check(pos_desejada,mapeamento_peças)
    

    peça_movendo.set_posi(pos_atual, pos_desejada)

    print(tab.get_estado())
    turno+=1