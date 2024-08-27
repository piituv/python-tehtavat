
b_sukupuoli = str(input("Biologinen sukupuoli: "))
hb_arvo = float(input("Hemoglobiinin arvo g/l: "))

if b_sukupuoli == "nainen" and hb_arvo in range(117,175):
    print("Hemoglobiini on normaali.")
elif b_sukupuoli == "nainen" and hb_arvo <117:
    print("Hemoglobiini on alahainen.")
elif b_sukupuoli == "nainen" and hb_arvo > 175:
    print("Hemoglobiini on korkea.")

if b_sukupuoli == "mies" and hb_arvo in range(134,195):
    print("Hemoglobiini on normaali.")
elif b_sukupuoli == "mies" and hb_arvo <134:
    print("Hemoglobiini on alahainen.")
elif b_sukupuoli == "mies" and hb_arvo > 195:
    print("Hemoglobiini on korkea.")
    