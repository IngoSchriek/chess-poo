from Classes_Xadrez import Peça, Tabuleiro
import numpy as np

tab = Tabuleiro()
p1 = Peça([4, 4], 'P1')
p2 = Peça([3, 4], 'P2')

dict = {}
dict[p1.get_nome()] = p1.get_posi()

tab.set_estado(dict)

print(tab.get_estado())



while True:
    peça = input('Peça: ')
    
    tab.set_estado({'--': dict[p1.get_nome()]})
    p1.set_posi(tab, list(map(int,input().split())))

    print(tab.get_estado())