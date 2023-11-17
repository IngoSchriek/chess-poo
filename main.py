from Classes_Xadrez import Peça, Tabuleiro, Cavalo, Rei
from utils import verifica_peça_no_tabuleiro,modifica_turno,check,destruidor

import numpy as np

turno=0

tab = Tabuleiro()

C1 = Cavalo([1, 4], 'C1', tab)
R = Rei([2, 4], 'R', tab)
C2 = Cavalo([3, 4], 'C2', tab)
c1 = Cavalo([1, 0], 'c1', tab)
r = Rei([2, 0], 'r', tab)
c2 = Cavalo([3, 0], 'c2', tab)

for x in range(len(tab.get_estado())):
    print(x, tab.get_estado()[x])
print('    0    1    2    3    4')

print(tab.get_mapeamento_peças())

while True:
    #pede a peça desejada e já deixa no do time tlgd
    if modifica_turno(turno, 'X').isupper():
        print(f'Turno: {turno}')
        print('Altas jogando.')
    else:
        print(f'Turno: {turno}')
        print('Baixas jogando.')

    peça_nome = modifica_turno(turno,input('Peça: ')).strip()
    peça_nome = verifica_peça_no_tabuleiro(tab.get_mapeamento_peças(), peça_nome)

    peça_movendo = tab.get_mapeamento_peças()[peça_nome]
    pos_atual = peça_movendo.get_posi()
    pos_desejada = list(map(int,input('Digite a posição desejada, para selecionar outra peça, digite -1: ').split()))
    if pos_desejada[0] == -1:
        #recomeça o loop
        continue
    if not peça_movendo.verifica(pos_desejada):
        print('Posição inválida. ')
        continue

    print(tab.get_mapeamento_peças())

    rei_turno=modifica_turno(turno,"R")
    mapeamento_backup = tab.get_mapeamento_peças()
    destruidor(tab.get_mapeamento_peças(),tab,pos_desejada)
    peça_movendo.set_posi(pos_atual, pos_desejada)
    posi_rei = tab.get_cord_peça(rei_turno)
    
    if check(posi_rei,tab.get_mapeamento_peças()):
        peça = tab.get_peça_cord(pos_desejada)
        peça_movendo.set_posi(pos_desejada, pos_atual)
        tab.set_estado({peça:pos_atual})
        tab.mapeamento_recover(mapeamento_backup)
        print('Seu rei está em cheque!')
        print('Lance inválido.')
        continue

    for x in range(len(tab.get_estado())):
        print(x, tab.get_estado()[x])
    print('    0    1    2    3    4')
    turno+=1