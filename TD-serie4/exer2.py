prix = float(input("saisir un prix HT :"))
tva = 0.2
if prix >= 200 :
    tva = 0.1

print(f" prix est {prix} , TVA = {tva} , TTC = " , tva * prix)
