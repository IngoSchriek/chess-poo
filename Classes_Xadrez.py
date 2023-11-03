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


class Peça:
    def __init__(self, posi: list, nome: str, tab: Tabuleiro) -> None:
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

"""
class Torre(Peça):
    def verifica(self, lance):
        posi_lista=self.posi
        if lance[0] in range(tab.tamanho()) and lance[0] in range(tab.tamanho()):
            #verifica o bagulho da torre não poder passar por cima dos manos e não comer aliados
            if lance!=posi_lista:
                if lance[0] == posi_lista[0]:
                    # for x in range()
    else:
        return False
                
            
class Rei(Peça):
    def verifica(self, lance):
        posi_lista=self.posi
        #gera as tres cordenadas horizontais que o rei pode acessar a partir da posição horizontal dele dele
        cord1, cord1[0], cord1[1]= [posi_lista[0]]*3, cord1[0]+1, cord1[0]-1
        cord2, cord2[0], cord2[1]=[posi_lista[1]]*3, cord2[0]+1, cord2[0]-1

        
        if (lance[0] in cord1 and lance[1] in cord2) and lance!=posi_lista:
            if lance[0] in range(tab.tamanho()) and lance[0] in range(tab.tamanho()):
                #verifica o bagulho do rei não comer aliados
                if
                    return True
    else:
        return False


low = {}
for x in range(9):
    low['t'+x] = Torre([]) 
"""