while 1 :
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    print("----------MENU----------")
    print("1--------Somme----------")
    print("2--------Produit--------")
    print("3--------Moyenne--------")
    print("4---------Minimum-------")
    print("5---------MAximum-------")
    print("-------------------------")
    op = int(input("donne nombre d'opperation :"))

    if op == 1:
        result = num1 + num2 + num3
        print("La somme des trois nombre est : ", result)

    elif op == 2:
        result = num1 * num2 * num3
        print("Le produit des trois nombre est : ", result)

    elif op == 3:
        result = num1 + num2 + num3
        result /= 3
        print("La moyenne des trois nombre est : ", result)

    elif op == 4:
        min = min(num1, num2, num3)
        print("Le min dex trois nombre est : ", min)

    elif op == 5:
        max = max(num1, num2, num3)
        print("Le max dex trois nombre est : ", max)
