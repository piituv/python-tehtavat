nimet= set()

while True:
    nimi= input("Anna nimi tai lopeta toimina painamalla Enter: ")

    if nimi == "":
        break

    if nimi in nimet:
        print("Anna uusi nimi.")
    else:
        print("Anna toinen nimi tai lopeta toimina painamalla Enter: ")
        nimet.add(nimi)

print("Annetut nimet:")
for nimi in nimet:
    print(nimi)

