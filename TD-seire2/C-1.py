MyArray = []
for i in range(10):
    print("Donne le numbre", i + 1, ": ")
    num = int(input())
    MyArray.append(num)

# Method 1 : MyArray [::-1]
newArray = MyArray[::-1]
print(newArray)


# Method 2 :
newArray = []
for i in range(10):
    newArray.append(MyArray[(len(MyArray) - 1) - i])
print(MyArray)
print(newArray)

