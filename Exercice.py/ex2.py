def sayHello(name , age):
    print("Bonjour" , name , "Your age is " , age)
name = input("Enter your name: ")
age = int(input("Enter your age: "))
sayHello(name , age)
print(" Name inverse ", name[::-1])