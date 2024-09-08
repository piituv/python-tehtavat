import random

def noppa():
    return random.randint(1,6)

def main():
    heitto=0
    while heitto!=6:
        heitto=noppa()
        print(heitto)
main ()