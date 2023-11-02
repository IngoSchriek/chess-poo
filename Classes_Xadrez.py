import numpy as np

class Tabuleiro:
    def __init__(self, **key_peça_posição, tamanho):
        self.tamanho = tamanho
        self.estado = np.array(['t1','t2','r','t3','t4'] + ['t'+str(x) for x in range(5,10)] + ['--']*5 + ['T'+str(x) for x in range(5,10)] + ['T1','T2','R','T3','T4']).reshape(5, 5)

    def tamanho(self):
        return tamanho


class Peça:
    def __init__(self, posi, cor):
        self.posi=posi
        self.cor=cor
    def cor(self):
        return self.cor
    def posi(self):
        return self.posi
    def posi_mod(self, pos):
        self.posi=pos
    def cor_mod(self, co):
        self.cor=co


class Torre(Peça):
    def verifica(self, lance):
        posi_lista=self.posi
            if lance[0] in range(tab.tamanho()) and lance[0] in range(tab.tamanho()):
                #verifica o bagulho da torre não poder passar por cima dos manos e não comer aliados
                if lance!=posi_lista:
                    if lance[0] == posi_lista[0]:
                        for x in range()
    else:
        return False
                
            
class Rei(Peça):
    def verifica(self, lance):
        posi_lista=self.posi
        #gera as tres cordenadas horizontais que o rei pode acessar a partir da posição horizontal dele dele
        cord1, cord1[0], cord1[1]=[posi_lista[0]]*3,cord1[0]+1,cord1[0]-1
        cord2, cord2[0], cord2[1]=[posi_lista[1]]*3,cord2[0]+1,cord2[0]-1

        
        if (lance[0] in cord1 and lance[1] in cord2) and lance!=posi_lista:
            if lance[0] in range(tab.tamanho()) and lance[0] in range(tab.tamanho()):
                #verifica o bagulho do rei não comer aliados
                if
                    return True
    else:
        return False


        
        