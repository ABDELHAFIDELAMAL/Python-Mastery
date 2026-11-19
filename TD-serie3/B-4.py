anne1 = int(input("Enter anne 1 :"))
mois1 = int(input("Enter le mois de anne 1:"))
jour1 = int(input("Enter le jour de anne 1:"))

anne2 = int(input("Enter anne 2 :"))
mois2 = int(input("Enter le mois de anne 1:"))
jour2 = int(input("Enter le jour de anne 1:"))

if anne1 > anne2:
    print("Lanne 1 est superieure de l anne 2")
elif anne2 > anne1:
    print("Lanne 2 est superieure de l anne 1")

elif anne1 == anne2 and mois1 > mois2:
    print("Lanne 1 est superieure de l anne 2")
elif anne1 == anne2 and mois2 > mois1 :
    print("Lanne 2 est superieure de l anne 2")

elif anne1 == anne2 and mois1 == mois2 and jour1 > jour2:
    print("Lanne 1 est superieure de l anne 2")
elif anne1 == anne2 and mois1 == mois2 and jour2 > jour1:
    print("Lanne 2 est superieure de l anne 1")
else :
    print("la date 1 est la meme date 2")
