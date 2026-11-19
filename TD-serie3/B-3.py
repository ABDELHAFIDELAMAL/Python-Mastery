a = int(input("Enter la valuer de a : "))
n = int(input("Enter la valuer de n : "))
result = 1
for i in range(n):
    result = result * a
print(f"{a} a la puissance de {n} = ", result)