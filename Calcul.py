class Person :

    def Person(self , name , familyname , age ):
        self.name = name
        self.age = age
        self.familyname = familyname


    def setname(self , name ):
        self.name = name
    def ToString(self):
        return f"{self.name} {self.familyname} {self.age} years old"
    def getName(self):
        return self.name







"""


def Addition(num1, num2) :
    if op == "+":
        return num1 + num2
def Subtraction(num1, num2) :
    if op == "-":
        return num1 - num2
def Multiplication(num1, num2) :
    if op == "*":
        return num1 * num2
def Division(num1, num2) :
    if op == "/":
        return num1 / num2
while 1 :
    num1 = float(input("Enter the first number: "))
    op = input("Enter the operation: ")
    num2 = float(input("Enter the second number: "))
    match op :
        case "+" :
            print("Result = " , Addition(num1, num2))
        case "-" :
            print("Result = " , Subtraction(num1, num2))
        case "*" :
            print("Result = " , Multiplication(num1, num2))
        case "/":
            print("==========\n" ,"Result = " , Division(num1, num2 ))
            
                
Age = int(input("Enter Age: "))
Sexe = input("Enter Sexe: ")
if Sexe == 'M' and Age >= 18:
    print("Voila! vous etes pait l'impot ")
elif Sexe == 'F' and Age <= 18 and Age >= 25 :
    print("Voila vous etes pait l'impot ")

"""