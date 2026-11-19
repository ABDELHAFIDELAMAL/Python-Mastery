MyList = []

while 1:
    num = float(input("Entrer un nombre: "))
    if num == 0 :
        break
    else :
        MyList.append(num)
if MyList == []:
    print("La liste est vide !")
else :
    print("les valeurs sont ", MyList)
    moyenne = sum(MyList) / len(MyList)
    print("La moyenne de la liste est ", moyenne)


