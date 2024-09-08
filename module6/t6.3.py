
def gallons_l(gallons):
    return gallons*3.785

def main():
    gallons= float(input("Anna nestegallonan maara: "))

    while gallons >= 0:
        litra = gallons_l(gallons)
        print(gallons, "gallonaa on", litra, "litraa.")
        gallons = float(input("Anna nestegallonan maara: "))

    print("Annettu maara on negatiivinen.")

main()

