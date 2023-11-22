from Classes_Xadrez import Peça, Tabuleiro, Cavalo, Rei, Torre, Dama, Bispo, Peão
from utils import verifica_peça_no_tabuleiro,modifica_turno,check,destruidor, evoluir

turno=0

tab = Tabuleiro(8)

# C1 = Cavalo([1, 4], 'C1', tab)
# C2 = Cavalo([3, 4], 'C2', tab)
# c1 = Cavalo([1, 0], 'c1', tab)
r = Rei([3, 0], 'r', tab)
c1=Cavalo([1,0], 'c1', tab)
c2=Cavalo([6,0], 'c2', tab)
b1=Bispo([2,0], 'b1', tab)
b2=Bispo([5,0], 'b2', tab)
d1=Dama([4,0],"d1", tab)
t1=Torre([0,0], 't1',tab)
t2=Torre([7,0], 't2',tab)

p1=Peão([0,1],'p1',tab)
p2=Peão([1,1],'p2',tab)
p3=Peão([2,1],'p3',tab)
p4=Peão([3,1],'p4',tab)
p5=Peão([4,1],'p5',tab)
p6=Peão([5,1],'p6',tab)
p7=Peão([6,1],'p7',tab)
p8=Peão([7,1],'p8',tab)


R = Rei([3, 7], 'R', tab)
C1=Cavalo([1,7], 'C1', tab)
C2=Cavalo([6,7], 'C2', tab)
B1=Bispo([2,7], 'B1', tab)
B2=Bispo([5,7], 'B2', tab)
D1=Dama([4,7],"D1", tab)
T1=Torre([0,7], 'T1',tab)
T2=Torre([7,7], 'T2',tab)

P1=Peão([0,6],'P1',tab)
P2=Peão([1,6],'P2',tab)
P3=Peão([2,6],'P3',tab)
P4=Peão([3,6],'P4',tab)
P5=Peão([4,6],'P5',tab)
P6=Peão([5,6],'P6',tab)
P7=Peão([6,6],'P7',tab)
P8=Peão([7,6],'P8',tab)



for x in range(len(tab.get_estado())):
    print(x, tab.get_estado()[x])
print('    0    1    2    3    4    5     6    7')

print(tab.get_mapeamento_peças())

Empate=False
while not(Empate):
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
    evoluir(tab,turno)

    for x in range(len(tab.get_estado())):
        print(x, tab.get_estado()[x])
    print('    0    1    2    3    4    5     6    7')
    turno+=1
if check_bool==True:
    print("C H E C K M A T E")
else:
    print("A F O G A M E N T O")