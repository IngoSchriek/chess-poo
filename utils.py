from Classes_Xadrez import Tabuleiro, Peça, Torre, Rei, Cavalo, Peão, Bispo

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
def checkmate(posição_rei, peças_dic,tab, turno):
    checkmate_bool=True
    lances=[]
    #gera todas as posições do tab
    for x in range(tab.tamanho):
        for y in range(tab.tamanho):
            lances.append([x,y])
    #pega todas as peças vivas
    for x in tab.get_mapeamento_peças.values():
        for y in lances:
            if x.verifica(y):
                pos_desejada=y
                pos_atual=x.get_posi()
                peça_movendo=x
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

def destruidor(dicionario:dict, tab:Tabuleiro, lance:list)->None:
    key=tab.get_peça_cord(lance)
    if key!="--":
        del dicionario[key]

def evoluir(tab, turno):
    peças_dicio=tab.get_mapeamento_peças()
    matrix=tab.get_estado()
    linhas_pontas=matrix[0]+matrix[tab.get_tamanho()-1]
    for x in linhas_pontas:
        if x[0]=="p" or x[0]=="P":
            escolha=Input("Qual peça e numero tu quer?EX: C0, T5, B2, d8")
            cordenada=tab.get_cord_peça(x)
            destruidor(peças_dicio,tab,cordenada)
            escolha=modifica_turno(turno, escolha)
            if escolha[0].upper()=="C":
                a=Cavalo(cordenada, escolha,tab)
            elif escolha[0].upper()=="B":
                a=Bispo(cordenada, escolha, tab)
            elif escolha[0].upper()=="T":
                a=Torre(cordenada,escolha, tab)
            else: 
                a=Dama(cordenada,escolha, tab)
    return a