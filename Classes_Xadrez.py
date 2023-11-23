import numpy as np

class Tabuleiro:
    def __init__(self, tamanho: int = 8) -> None:
        self.tamanho = tamanho
        self.estado = np.array(['--']*(self.tamanho**2)).reshape(self.tamanho, self.tamanho)
        self.mapeamento_peças = {}

    def get_tamanho(self) -> int:
        return self.tamanho

    def get_cord_peça(self, peça_nome)-> list:
        return  self.get_mapeamento_peças()[peça_nome].get_posi()

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

    def set_mapeamento_peças(self, nome_peça, obj_peça):
        self.mapeamento_peças[nome_peça] = obj_peça

    def mapeamento_recover(self, mapeamento):
        self.mapeamento_peças = mapeamento

    def get_mapeamento_peças(self):
        return self.mapeamento_peças
    
class Peça:
    def __init__(self, posi: list, nome: str, tab: Tabuleiro) -> None:
        # (x,y)
        self.posi=posi
        self.nome=nome
        #posição inicial
        self.tab=tab
        self.lances_possiveis = []
        tab.set_estado({nome:posi})
        tab.set_mapeamento_peças(self.nome, self)

    def get_nome(self) -> str:
        return self.nome

    def get_posi(self) -> list:
        return self.posi

    def set_posi(self, pos_anterior: list, pos_desejada: list) -> None:
        self.posi=pos_desejada
        self.tab.set_estado({'--': pos_anterior})
        self.tab.set_estado({self.nome: pos_desejada})
        
    def set_nome(self, nome: str) -> None:
        self.nome=nome
    
    def verifica(self) -> True:
        return True

    def dentro_tab(self, cord: list)->bool:
        positivo=cord[0]>=0 and cord[1]>=0
        dentro= cord[0] < self.tab.tamanho and cord[1] < self.tab.tamanho
        if positivo and dentro:
            return True
        else:
            return False

    def get_lances_possiveis(self) -> list:
        return self.lances_possiveis
    
    def set_lances_possiveis(self, lances_possiveis: list) -> None:
        self.lances_possiveis = lances_possiveis

class Torre(Peça):
    def verifica(self, lance: list) -> bool:
        x,y= self.posi
        lances_possiveis = []
        
        #para cima
        for i in range(1,self.tab.get_tamanho()):
            if y+i < self.tab.get_tamanho():
                if self.tab.get_peça_cord([x,y+i]) != '--':
                    if self.get_nome().isupper() != self.tab.get_peça_cord([x,y+i]).isupper():
                        lances_possiveis.append([x,y+i])
                    break
                else:
                    lances_possiveis.append([x,y+i])
        
        #para baixo
        for i in range(1,self.tab.get_tamanho()):
            if y-i >= 0:
                if self.tab.get_peça_cord([x,y-i]) != '--':
                    if self.get_nome().isupper() != self.tab.get_peça_cord([x,y-i]).isupper():
                        lances_possiveis.append([x,y-i])
                    break
                else:
                    lances_possiveis.append([x,y-i])
        
        #para direita
        for i in range(1,self.tab.get_tamanho()):
            if x+i < self.tab.get_tamanho():
                if self.tab.get_peça_cord([x+i,y]) != '--':
                    if self.get_nome().isupper() != self.tab.get_peça_cord([x+i,y]).isupper():
                        lances_possiveis.append([x+i,y])
                    break
                else:
                    lances_possiveis.append([x+i,y])

        #para esquerda
        for i in range(1,self.tab.get_tamanho()):
            if x-i >= 0:
                if self.tab.get_peça_cord([x-i,y]) != '--':
                    if self.get_nome().isupper() != self.tab.get_peça_cord([x-i,y]).isupper():
                        lances_possiveis.append([x-i,y])
                    break
                else:
                    lances_possiveis.append([x-i,y])
                    
        self.set_lances_possiveis(lances_possiveis)
        if lance in lances_possiveis:
            return True
        else:
            return False

class Rei(Peça):
    def verifica(self, lance):
        posi_lista=self.posi
        lances_possiveis = []

        lances_rei = [[-1, -1],[-1, 0],[-1, 1],[0, -1],[0, 1],[1, -1],[1, 0],[1, 1]]
        for x in lances_rei:
            lance_candidato = [posi_lista[0]+x[0],posi_lista[1]+x[1]]
            if lance_candidato != posi_lista \
                and self.dentro_tab(lance_candidato) \
                    and (self.tab.get_peça_cord(lance_candidato)=='--' or
                         self.tab.get_peça_cord(lance)[0].isupper()!=self.nome[0].isupper()):
                lances_possiveis.append(lance_candidato)

        self.set_lances_possiveis(lances_possiveis)
        if lance in lances_possiveis:
            return True
        else:
            return False

class Cavalo(Peça):
    def verifica(self, lance: list) -> bool:
        posi_lista=self.posi
        #lances que um cavalo pode somar para a posição atual dele
        lances_cavalo=[[2,1],[-2,1],[2,-1],[-2,-1],
        [1,2],[-1,2],[1,-2],[-1,-2]]

        # soma todos os possiveis lances e armazena numa lista aqueles que
        # cumprem com os requisitos para lance válido
        lances_possiveis=[]
        for x in lances_cavalo:
            lance_candidato = [posi_lista[0]+x[0],posi_lista[1]+x[1]]
            if lance_candidato != posi_lista \
                and self.dentro_tab(lance_candidato) \
                    and (self.tab.get_peça_cord(lance_candidato)=='--' or
                         self.tab.get_peça_cord(lance)[0].isupper()!=self.nome[0].isupper()):
                lances_possiveis.append(lance_candidato)

        self.set_lances_possiveis(lances_possiveis)
        if lance in lances_possiveis:
            return True
        else:
            return False
        
class Peão(Peça):
    def verifica(self, lance: list) -> bool:
        posi_lista=self.posi
        #lances que um peao pode somar para a posição atual dele
        if self.get_nome().isupper():
            if posi_lista[1]==6:
                lances_peão=[[-1,-1],[0,-1],[1,-1],[0,-2]]
            else:
                lances_peão=[[-1,-1],[0,-1],[1,-1]]
        else:
            if posi_lista[1]==1:
                lances_peão=[[-1,1],[0,1],[1,1],[0,2]]
            else:
                lances_peão=[[-1,1],[0,1],[1,1]]

        # soma todos os possiveis lances e armazena numa lista todos aqueles que
        # cumprem as condiçoes para lance válido
        lances_possiveis=[]
        for x in lances_peão:
            lance_candidato = [posi_lista[0]+x[0],posi_lista[1]+x[1]]
            if lance_candidato != posi_lista \
                and self.dentro_tab(lance_candidato) \
                    and (self.tab.get_peça_cord(lance_candidato)=='--' or
                         self.tab.get_peça_cord(lance)[0].isupper()!=self.nome[0].isupper()):
                lances_possiveis.append(lance_candidato)

        self.set_lances_possiveis(lances_possiveis)
        if lance in lances_possiveis:
            return True
        else:
            return False

class Bispo(Peça):
    def verifica(self, lance: list) -> bool:
        x,y= self.posi
        lances_possiveis = []
        
        #para cima e direita
        for i in range(1,self.tab.get_tamanho()):
            if x+i < self.tab.get_tamanho() and y+i < self.tab.get_tamanho():
                if self.tab.get_peça_cord([x+i,y+i]) != '--':
                    if self.get_nome().isupper() != self.tab.get_peça_cord([x+i,y+i]).isupper():
                        lances_possiveis.append([x+i,y+i])
                    break
                else:
                    lances_possiveis.append([x+i,y+i])
        
        #para baixo e direta
        for i in range(1,self.tab.get_tamanho()):
            if x+i < self.tab.get_tamanho() and y-i >= 0:
                if self.tab.get_peça_cord([x+i,y-i]) != '--':
                    if self.get_nome().isupper() != self.tab.get_peça_cord([x+i,y-i]).isupper():
                        lances_possiveis.append([x+i,y-i])
                    break
                else:
                    lances_possiveis.append([x+i,y-i])
        
        #para cima e esquerda
        for i in range(1,self.tab.get_tamanho()):
            if x-i >= 0 and y+i < self.tab.get_tamanho():
                if self.tab.get_peça_cord([x-i,y+i]) != '--':
                    if self.get_nome().isupper() != self.tab.get_peça_cord([x-i,y+i]).isupper():
                        lances_possiveis.append([x-i,y+i])
                    break
                else:
                    lances_possiveis.append([x-i,y+i])

        #para baixo e esquerda
        for i in range(1,self.tab.get_tamanho()):
            if x-i >= 0 and y-i>=0:
                if self.tab.get_peça_cord([x-i,y-i]) != '--':
                    if self.get_nome().isupper() != self.tab.get_peça_cord([x-i,y-i]).isupper():
                        lances_possiveis.append([x-i,y-i])
                    break
                else:
                    lances_possiveis.append([x-i,y-i])
        
        self.set_lances_possiveis(lances_possiveis)
        if lance in lances_possiveis:
            return True
        else:
            return False
        

class Dama(Peça):
    def verifica(self, lance: list) -> bool:
        x,y= self.posi
        lances_possiveis = []
        
        #para cima e direita
        for i in range(1,self.tab.get_tamanho()):
            if x+i < self.tab.get_tamanho() and y+i < self.tab.get_tamanho():
                if self.tab.get_peça_cord([x+i,y+i]) != '--':
                    if self.get_nome().isupper() != self.tab.get_peça_cord([x+i,y+i]).isupper():
                        lances_possiveis.append([x+i,y+i])
                    break
                else:
                    lances_possiveis.append([x+i,y+i])
        
        #para baixo e direta
        for i in range(1,self.tab.get_tamanho()):
            if x+i < self.tab.get_tamanho() and y-i >= 0:
                if self.tab.get_peça_cord([x+i,y-i]) != '--':
                    if self.get_nome().isupper() != self.tab.get_peça_cord([x+i,y-i]).isupper():
                        lances_possiveis.append([x+i,y-i])
                    break
                else:
                    lances_possiveis.append([x+i,y-i])
        
        #para cima e esquerda
        for i in range(1,self.tab.get_tamanho()):
            if x-i >= 0 and y+i < self.tab.get_tamanho():
                if self.tab.get_peça_cord([x-i,y+i]) != '--':
                    if self.get_nome().isupper() != self.tab.get_peça_cord([x-i,y+i]).isupper():
                        lances_possiveis.append([x-i,y+i])
                    break
                else:
                    lances_possiveis.append([x-i,y+i])

        #para baixo e esquerda
        for i in range(1,self.tab.get_tamanho()):
            if x-i >= 0 and y-i>=0:
                if self.tab.get_peça_cord([x-i,y-i]) != '--':
                    if self.get_nome().isupper() != self.tab.get_peça_cord([x-i,y-i]).isupper():
                        lances_possiveis.append([x-i,y-i])
                    break
                else:
                    lances_possiveis.append([x-i,y-i])
                    
        #para cima
        for i in range(1,self.tab.get_tamanho()):
            if y+i < self.tab.get_tamanho():
                if self.tab.get_peça_cord([x,y+i]) != '--':
                    if self.get_nome().isupper() != self.tab.get_peça_cord([x,y+i]).isupper():
                        lances_possiveis.append([x,y+i])
                    break
                else:
                    lances_possiveis.append([x,y+i])
        
        #para baixo
        for i in range(1,self.tab.get_tamanho()):
            if y-i >= 0:
                if self.tab.get_peça_cord([x,y-i]) != '--':
                    if self.get_nome().isupper() != self.tab.get_peça_cord([x,y-i]).isupper():
                        lances_possiveis.append([x,y-i])
                    break
                else:
                    lances_possiveis.append([x,y-i])
        
        #para direita
        for i in range(1,self.tab.get_tamanho()):
            if x+i < self.tab.get_tamanho():
                if self.tab.get_peça_cord([x+i,y]) != '--':
                    if self.get_nome().isupper() != self.tab.get_peça_cord([x+i,y]).isupper():
                        lances_possiveis.append([x+i,y])
                    break
                else:
                    lances_possiveis.append([x+i,y])

        #para esquerda
        for i in range(1,self.tab.get_tamanho()):
            if x-i >= 0:
                if self.tab.get_peça_cord([x-i,y]) != '--':
                    if self.get_nome().isupper() != self.tab.get_peça_cord([x-i,y]).isupper():
                        lances_possiveis.append([x-i,y])
                    break
                else:
                    lances_possiveis.append([x-i,y])
        
        self.set_lances_possiveis(lances_possiveis)
        if lance in lances_possiveis:
            return True
        else:
            return False

