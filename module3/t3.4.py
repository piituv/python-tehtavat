
k_vuosi = float(input("Vuosiluku: "))

if (k_vuosi%4==0) or ((k_vuosi%100)%400==0):
    print("On karkausvuosi.")
else:
    print("Ei ole karkausvuosi.")

