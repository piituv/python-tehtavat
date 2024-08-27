
hyttiluokka = str(input("Anna laivan hyttiluokka: ")).upper()

hytti_lux = "Hytti on parvekkeellinen hytti yläkannella."
hytti_A = "Hytti on ikkunallinen hytti autokannen yläpuolella."
hytti_B = "Hytti on ikkunaton hytti autokannen yläpuolella."
hytti_C = "Hytti on ikkunaton hytti autokannen alapuolella."

if hyttiluokka == "LUX":
    print(hytti_lux)
elif hyttiluokka == "A":
    print(hytti_A)
elif hyttiluokka == "B":
    print(hytti_B)
elif hyttiluokka == "C":
    print(hytti_C)
else:
    print("Virheellinen hyttiluokka.")
