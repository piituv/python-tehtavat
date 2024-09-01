#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

luku = random.randint(1,10)



while True:
    arvaa = int(input("Arvaa luku välilta 1 - 10: "))

    if arvaa < luku:
        print("Liian pieni arvaus.")
    elif arvaa > luku:
        print("Liian suuri arvaus.")
    else:
        print("Oikein.")
        break




