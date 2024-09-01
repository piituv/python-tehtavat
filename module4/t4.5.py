yritys = 0
kayttajatunnus = "python"
salasana = "rules"

while yritys <= 5:
    kayttajatunnus = input("Anna kayttajatunnus:")
    salasana = input("Anna salasana:")

    if kayttajatunnus == "python" and salasana == "rules":
        print("Tervetuola.")
        break

    else:
        print("Vaara kayttaja tai salasana, yrita uudelleen.")
        yritys += 1

if yritys >= 5:
    print ("Paasy evatty.")
















