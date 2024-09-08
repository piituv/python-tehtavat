import random

def noppa(noppa_silmaluku):
    return random.randint(1,noppa_silmaluku)

def main():
    noppa_silmaluku = int(input("Anna nopan silmalukujen maara: "))

    heitto=0
    while heitto!= noppa_silmaluku:
        heitto=noppa(noppa_silmaluku)
        print(heitto)


main ()