from turtledemo.paint import switchupdown

MyList = []
for i in range(10):
    print("Donne valeur de [", i + 1 ,"] : " , end="")
    num = int(input())
    MyList.append(num)
Max = max(MyList)
Min = min(MyList)
print("Max =", Max)
print("Min =", Min)
