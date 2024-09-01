numbers = []

while True:
    syota_luku = input("Syötä luku: ")
    if syota_luku == "":
        break

    numbers.append(float(syota_luku))


if numbers:
    print(f"Pienin luku on : {min(numbers)}")
    print(f"Suurin luku on : {max(numbers)}")
else:
    print("Ei syotettyja lukuja.")
