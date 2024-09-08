#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def summa(luvut_lista):
    return sum(luvut_lista)

def main():
    luvut= [3,4,5,6,66,98]
    yhteensa = summa(luvut)
    print("Summa on:", yhteensa)

main()