n = int(input("Donne la taille de la liste : "))
MyList = []

for i in range(n):
    print("Donne la valuer de List[", i+1 , "] : ")
    num = float(input())
    MyList.append(num)

if len(MyList) == 0 :
    print("La liste est vide !")
else :
    moyenne = sum(MyList) / len(MyList)
    print("La moyenne de la liste est ", moyenne)
