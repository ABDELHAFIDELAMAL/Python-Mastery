chaine = input("Donne une chaine : ")
c = input("Donne une caractere : ")

for i in range(len(chaine)):
    if chaine[i] == c :
        print(f"L indice de {c} dans {chaine} est :", i)
        break

result = chaine.count(c , 0 , -1)
print(f"nombre de {c} dans {chaine} est :" , result)
