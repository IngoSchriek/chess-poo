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
    for x in peças_dic.value():
        if x.verifica(posição_rei)== True:
            contador+=1
    if x!=0:
        return True
    else:
        return False

        