from Classes_Xadrez import Tabuleiro, Peça, Torre, Rei, Cavalo, Peão, Bispo, Dama
import numpy as np


def verifica_peça_no_tabuleiro(peças_vivas: dict, peça_desejada: str) -> str:
    while not peça_desejada in peças_vivas:
        print('Peça não encontrada no tabuleiro. ')
        peça_desejada = input('Peça: ')
    return peça_desejada

def modifica_turno(turno: int, peça: str) -> str:
    if turno%2==0:
        return peça.upper()
    else:
        return peça.lower()

def check(tab: Tabuleiro, turno: int) -> bool:
    contador=0
    rei_turno=modifica_turno(turno,"R")
    posição_rei = tab.get_cord_peça(rei_turno)
    peças_dic = tab.get_mapeamento_peças()
    peças_inimigas_dic = {k: v for k, v in peças_dic.items() if k.isupper() != rei_turno.isupper()}
    for x in peças_inimigas_dic.values():
        if x.verifica(posição_rei)== True:
            contador+=1
    if contador!=0:
        return True
    else:
        return False

def checkmate_empate(tab: Tabuleiro, turno: int) -> bool:
    checkmate_bool=True
    rei_turno=modifica_turno(turno,"R")
    peças = {v for k, v in tab.get_mapeamento_peças().items() if k.isupper() == rei_turno.isupper()}
    for peça_testando in peças:
        peça_testando.verifica([0,0])
        for lance in peça_testando.get_lances_possiveis():
            pos_desejada=lance
            pos_atual=peça_testando.get_posi()
            peça_movendo=peça_testando
            mapeamento_backup = dict(tab.get_mapeamento_peças())
            peça = tab.get_peça_cord(pos_desejada)
            destruidor(tab,pos_desejada)
            peça_movendo.set_posi(pos_atual, pos_desejada)

            if check(tab, turno):
                peça_movendo.set_posi(pos_desejada, pos_atual)
                tab.set_estado({peça:pos_desejada})
                tab.mapeamento_recover(mapeamento_backup)

            else:
                checkmate_bool=False
                peça_movendo.set_posi(pos_desejada, pos_atual)
                tab.set_estado({peça:pos_desejada})
                tab.mapeamento_recover(mapeamento_backup)
                break
        if checkmate_bool == False:
            break
    return checkmate_bool

def destruidor(tab:Tabuleiro, lance:list)->None:
    key=tab.get_peça_cord(lance)
    if key!="--":
        del tab.get_mapeamento_peças()[key]

def evoluir(tab, turno):
    peças_dicio=tab.get_mapeamento_peças()
    matrix=tab.get_estado()
    linha_de_chegada = matrix[0].tolist()+matrix[tab.get_tamanho()-1].tolist()
    for x in linha_de_chegada:
        if x[0]=="p" or x[0]=="P":
            escolha=input("Qual peça e numero tu quer?EX: C0, T5, B3, d8 ")
            escolha=modifica_turno(turno, escolha)
            while escolha in peças_dicio:
                print('É necessário que a peça tenha nome único.')
                escolha = input("Qual peça e numero tu quer? ")
                escolha=modifica_turno(turno, escolha)
            cordenada=tab.get_cord_peça(x)
            destruidor(tab,cordenada)
            if escolha[0].upper()=="C":
                x=Cavalo(cordenada, escolha,tab)
            elif escolha[0].upper()=="B":
                x=Bispo(cordenada, escolha, tab)
            elif escolha[0].upper()=="T":
                x=Torre(cordenada,escolha, tab)
            else: 
                x=Dama(cordenada,escolha, tab)

