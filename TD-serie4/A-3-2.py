def estPremier(n):
    if n <= 1 :
        return False
    elif n == 2:
        return True
    else:
        esrTrue = True
        for i in range( 2 , ( n//2 ) + 1 ):
            if n % i == 0:
                esrTrue = False
                break
        if esrTrue :
            return True
        else:
            return False
MyList = []
for i in range(2 , 101):
    if estPremier(i):
        MyList.append(i)
print("Les nombres premier de 2 a 100 est : \n" ,MyList)