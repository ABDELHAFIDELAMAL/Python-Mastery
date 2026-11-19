ch1 = input("Entrer la chaine N1 : ")
ch2 = input("Entrer la chaine N2 : ")

if len(ch1) > len(ch2):
    print(1)
elif len(ch1) == len(ch2):
    print(0)
elif len(ch1) < len(ch2):
    print(-1)