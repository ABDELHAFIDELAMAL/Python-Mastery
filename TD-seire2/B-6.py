while True :
    nombre = int(input("Entrez un nombre : "))

    if nombre <= 1:
        print("La nombre est non premier ")
    elif nombre == 2:
        print("La nombre est premier ")
    else:
        estTrue = True
        for i in range(2, nombre , 1):
            if nombre % i == 0:
                estTrue = False
                break
        if estTrue:
            print("La nombre est premier ")
        else:
            print("La nombre non premier ")





