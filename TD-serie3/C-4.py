while 1 :
    Login = input("Donne votre Login: ")
    Password = input("Donne votre Password: ")

    if Login.find("@gmail.com" or "@ucd.ac.ma" , -10 , -1) and len(Password) >= 8:
        print("Connection reussit")
        break
    else :
        print("votre donnee est incorrect!")
        continue
