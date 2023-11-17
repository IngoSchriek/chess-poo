import utils
import numpy as np

class Tabuleiro:
    def __init__(self, tamanho: int = 5) -> None:
        self.tamanho = tamanho
        self.estado = np.array(['--']*25).reshape(5, 5)
        # self.estado = np.array_split(['t1','t2','r','t3','t4'] +
        #                              ['t'+str(x) for x in range(5,10)] +
        #                              ['--']*5 + ['T'+str(x) for x in range(5,10)] + 
        #                              ['T1','T2','R','T3','T4'], 5)

    def get_tamanho(self) -> int:
        return self.tamanho

    def get_estado(self) -> np.array:
        return self.estado

    def set_estado(self, posiçoes: dict) -> None:
        for peça, cord in posiçoes.items():
            x,y = cord
            self.estado[y][x] = peça
    
    def get_peça_cord(self, cord)-> str:
        x,y=cord
        return self.estado[y][x]
    
    def dentro_tab(self, cord)->bool:
        positivo=cord[0]>=0 and cord[1]>=0
        dentro=cord[0]<=self.tamanho and cord[1]<=self.tamanho
        if positivo and dentro:
            return True
        else:
            return False



class Peça:
    def __init__(self, posi: list, nome: str, tab: Tabuleiro) -> None:
        # (x,y)
        self.posi=posi
        self.nome=nome
        #posição inicial
        self.tab=tab
        tab.set_estado({nome:posi})

    def get_nome(self) -> str:
        return self.nome

    def get_posi(self) -> list:
        return self.posi

    def set_posi(self, pos_anterior, pos_desejada) -> None:
        self.posi=pos_desejada
        self.tab.set_estado({'--': pos_anterior})
        self.tab.set_estado({self.nome: pos_desejada})
        
    def set_nome(self, nome) -> None:
        self.nome=nome

class Torre(Peça):
    def verifica(self, lance):
        posi_lista=self.posi
        if tab.dentro_tab(lance):
            #verifica o bagulho da torre não poder passar por cima dos manos e não comer aliados
            if lance!=posi_lista:
                if lance[0] == posi_lista[0]:
                    for x in range(min(posi_lista[1],lance[1])+1, max(posi_lista[1],lance[1])-1):
                        if tab.get_peça_cord([posi_lista[0],x])=="--":
                            if get_peça_cord(lance)=='--':
                                return True
                            else:
                                if tab.get_peça_cord(lance)[0].isupper()!=self.nome[0].isupper(): 
                                    return True
        else:
            return False

class Rei(Peça):

    def verifica(self, lance):
        posi_lista=self.posi
        #gera as tres cordenadas horizontais e verticais que o rei pode acessar a partir da posição horizontal dele dele
        posi_horizontal = [posi_lista[0]+1, posi_lista[0]-1, posi_lista[0]]
        posi_vertical = [posi_lista[1]+1, posi_lista[1]-1, posi_lista[1]]

        #vê se o rei ta querendo se mover pra casa valida gerada anteriormente
        if (lance[0] in posi_horizontal and lance[1] in posi_vertical) and lance!=posi_lista:

            #ve se o rei não quer sair do tabuleiro
            if self.dentro_tab(lance):

                #olha o tab pra ver se o slot ta desocupado sla
                if tab.get_peça_cord(lance)=='--':
                    return True

                #olha pra ver se os times são diferentes se ten alguem ocupando o slot
                else:
                    if tab.get_peça_cord(lance).isupper()!=self.nome.isupper(): 
                        return True

        else:
            return False


class Cavalo(Peça):
    def verifica(self, lance):
        posi_lista=self.posi
        #lances que um cavalo pode somar para a posição atual dele
        lances_cavalo=[[2,1],[-2,1],[2,-1],[-2,-1],
        [1,2],[-1,2],[1,-2],[-1,-2]]
        #soma todos os possiveis lances e armazena numa lista
        lances_possiveis=[]
        for x in lances_cavalo:
            lances_possiveis.append([posi_lista[0]+x[0],posi_lista[1]+x[1]])
        #vê se o cavalo ta querendo se mover pra casa valida gerada anteriormente
        if (lance in lances_possiveis) and lance!=posi_lista:
            #ve se o cavalo não quer sair do tabuleiro
            if self.dentro_tab(tab.tamanho()):
                #olha o tab pra ver se o slot ta desocupado sla
                if tab.get_peça_cord(lance)=='--':
                    return True
                #olha pra ver se os times são diferentes se ten alguem ocupando o slot
                else:
                    if tab.get_peça_cord(lance)[0].isupper()!=self.nome[0].isupper(): 
                        return True
        else:
            return False