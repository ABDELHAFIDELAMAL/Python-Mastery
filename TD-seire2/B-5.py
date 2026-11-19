num1 = float(input("Entre un numero 1 : "))
num2 = float(input("Entre un numero 2 : "))
num3 = float(input("Entre un numero 3 : "))

if num1 > num2 and num1 > num3 :
    print("Max est num1 : " , num1)
elif num2 > num1 and num2 > num3 :
    print("Max est num2 : " , num2)
else:
    print("Max est num3 : " , num3)
