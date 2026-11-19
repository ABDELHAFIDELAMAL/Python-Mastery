def recherche_dichotomique(MyList, n):
    MyList.sort()
    debut = 0
    fin = len(MyList) - 1

    index = (fin + debut) // 2

    if n >= MyList[index]:
        for i in range(index, fin + 1):
            if n == MyList[i]:
                return i+1
        return "Non exist"
    else:
        for i in range(debut, index):
            if n == MyList[i]:
                return i+1
        return "Non exist"


MyList = [1, 3, 4, 5, 7, 10]
n = 7
print(recherche_dichotomique(MyList, n))
