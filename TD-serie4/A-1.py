def Puissance( n , p):
    if p == 0 :
        return 1
    elif p > 0 :
        result = 1
        for i in range(1,p+1):
            result *= n
        return result
    else :
        return 1 / Puissance(n ,-p)

n = float(input("Enter nombre n : "))
p = int(input("Enter p : "))

print(f"{n} a La puissance de {p} est =", Puissance(n,p))
