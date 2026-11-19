MyList = []
a = "abcdefj"
while True:
    valeur = input("Donne un nombre : ")

    if not valeur.isdigit() :
        print("Arrêt de la saisie.")
        break

    MyList.append(int(valeur))

print("Les nombres saisis sont :", MyList)
print("La taille de la liste est : " , len(MyList))

