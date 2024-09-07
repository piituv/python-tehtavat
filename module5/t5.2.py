luvut = []
luku = 0

while luku != "":
    syotto = (input("Anna luku: "))

    if syotto == "":
        print("Toiminta lopetettu.")
        break
    luku = float(syotto)
    luvut.append(luku)

luvut.sort(reverse=True)
print("Viisi suurinta lukua ovat:", luvut[:5])
