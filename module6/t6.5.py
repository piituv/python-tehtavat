def pariton_lista(lista):
    parilliset=[]

    for luku in lista:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset


def main():
    luvut_lista =[22,23,45,65,77,8,98,654,243,1,987]
    parilliset=pariton_lista(luvut_lista)

    print("Koko lista: ", luvut_lista)
    print("Parilliset: ", parilliset)

main()

