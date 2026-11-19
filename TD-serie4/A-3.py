def estPremier(n):
    if n <= 1 :
        print(n , "est non premier")
    elif n == 2:
        print(n , "est premier")
    else:
        esrTrue = True
        for i in range( 2 , ( n//2 ) + 1 ):
            if n % i == 0:
                esrTrue = False
                break
        if esrTrue :
            print(n , "est premier")
        else:
            print(n , "est non premier")

n = int(input("Enter nombre n : "))
estPremier(n)