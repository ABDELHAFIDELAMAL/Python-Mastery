def raccorder(list):
    chaine = ""
    for i in list:
        chaine += " "
        chaine += str(i)
    return "\'"+ chaine + "\'"

mylist = ["hello" , "world" , "!" , 123]
print(raccorder(mylist))