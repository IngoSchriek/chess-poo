from Classes_Xadrez import Peça, Tabuleiro


def verifica_peça_no_tabuleiro(peças, peça_desejada):
    while not peça_desejada in peças:
        print('Peça não encontrada no tabuleiro. ')
        peça_desejada = input('Peça: ')
    return peça_desejada
def modifica_turno(turno, peça):
    if turno%2==0:
        return peça.upper()
    else:
        return peça.lower()

def check(posição_rei, peças_dic):
    contador=0
    for x in peças_dic.values():
        if x.verifica(posição_rei)== True:
            contador+=1
    if contador!=0:
        return True
    else:
        return False

# def checkmate(tabuleiro, turno, dicionario):
#     tabuleiro2=tabuleiro
#     for x in dicionario(values):
#         if x.get_nome()[0]==:
#             for y in posições:
                

def destruidor(dicionario:dict, tab:Tabuleiro, lance:list)->None:
    key=tab.get_peça_cord(lance)
    if key!="--":
        del dicionario[key]

        