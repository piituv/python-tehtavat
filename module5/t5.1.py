
import random

arpakuutio_maara = 0

arpakuutio = int(input("Anna arpakuutioiden lukumaara: "))

for _ in range(arpakuutio):
    heitto = random.randint(1,6)
    arpakuutio_maara += heitto

print("Silmalukujen summa on:", arpakuutio_maara)




