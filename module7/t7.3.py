
def main():
    # Dictionary to store airport information
    airports = {}

    while True:

        print("1. Lisää uusi lentoasema")
        print("2. Hae lentoasema")
        print("3. Lopeta")

        choice = input("Valiste toiminto (1,2,3):  ")

        if choice == '1':
            icao_code = input("Anna ICAO koodi: ").upper()
            name = input("Anna lentoaseman nimi: ")
            airports[icao_code] = name
            print("Lentoasema lisätty")

        elif choice == '2':
            icao_code = input("Anna ICAO koodi: ").upper()
            if icao_code in airports:
                print(f"Lentoasema jonka ICAO koodi on: {icao_code} on {airports[icao_code]}.")
            else:
                print("Tietoa ei löytynyt.")

        elif choice == '3':
            print("Toiminta lopetettu.")
            break

main()

