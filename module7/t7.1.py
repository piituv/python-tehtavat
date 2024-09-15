
vuodenajat = ("kevat","kesa", "syksy", "talvi")

kuukausi = input("Anna kuukauden numero: ")

if kuukausi in ("12", "1", "2"):
    vuodenaika = vuodenajat[3]
elif kuukausi in ("3","4","5"):
    vuodenaika = vuodenajat[0]
elif kuukausi in ("6","7","8"):
    vuodenaika = vuodenajat[1]
elif kuukausi in ("9","10","11"):
    vuodenaika = vuodenajat[2]
else:
    print("Ei ole kuukausi.")

print("Kuukauden vastaava vudenaika on:", vuodenaika)