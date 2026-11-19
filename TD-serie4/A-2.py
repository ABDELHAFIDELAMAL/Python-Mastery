def raccorder(list):
    chaine = ""
    for i in list:
        chaine += str(i)
    return "\'"+ chaine + "\'"

mylist = ["hello" , "world" , 1]
print(raccorder(mylist))