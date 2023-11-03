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
print("--".isupper())