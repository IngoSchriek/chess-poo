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

#tem q adaptar esse bagulho de ir e voltar o tabuleiro e não sei se o Break funciona assim
def checkmate(posição_rei, peças_dic,tab):
    checkmate_bool=True
    lances=[]
    #gera todas as posições do tab
    for x in range(tab.get_tamanho()):
        for y in range(tab.get_tamanho()):
            lances.append([x,y])
    #pega todas as peças vivas
    for x in tab.get_mapeamento_peças().values():
        for y in lances:
            if x.verifica(y):
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

                else:
                    checkmate_bool=False
                    peça = tab.get_peça_cord(pos_desejada)
                    peça_movendo.set_posi(pos_desejada, pos_atual)
                    tab.set_estado({peça:pos_atual})
                    tab.mapeamento_recover(mapeamento_backup)
                    break



# def checkmate(tabuleiro, turno, dicionario):
#     tabuleiro2=tabuleiro
#     for x in dicionario(values):
#         if x.get_nome()[0]==:
#             for y in posições:
                

def destruidor(dicionario:dict, tab:Tabuleiro, lance:list)->None:
    key=tab.get_peça_cord(lance)
    if key!="--":
        del dicionario[key]

        