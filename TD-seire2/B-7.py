import math
print(" Lequation est : a * x ** 2 + b * x + c = 0 ")
a = int(input("Saisie  'a'  de l'equoition quadratique : "))
b = int(input("Saisie  'b'  de l'equoition quadratique : "))
c = int(input("Saisie  'c'  de l'equoition quadratique : "))

delta = b**2 - 4*a*c

if delta < 0 :
    print("l'equation aucun solution reel")
if delta == 0:
    result = -b /(2*a)
    print("Result =",result)
else:
    result1 = (-b + math.sqrt(delta))/(2*a)
    result2 = (-b - math.sqrt(delta))/(2*a)
    print("Il y a deux resultat : ")
    print("Result 1 =",result1)
    print("Result 2 =",result2)