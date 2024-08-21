#Yksi leiviskä on 20 naulaa.
#Yksi naula on 32 luotia.
#Yksi luoti on 13,3 grammaa.

LUOTI = 13.3
NAULA = LUOTI*32
LEIVISKA = 20*NAULA

luoti = int(input("Luotien maara: "))
naula = int(input("Naulojen maara: "))
leiviska = int(input("Leiviskojen maara: "))

massa = float(LUOTI*luoti+NAULA*naula+LEIVISKA*leiviska)

print(f"Kokonaismassa on:", massa/1000, "kg")
