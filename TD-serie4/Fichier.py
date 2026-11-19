File = open("Fichier.txt", "a+" , encoding="utf-8")

File.write("id,prenom,nom,note\n")
# => Write dans Fichier
id = 0
for i in range(3):
    id += 1
    newID = str(id)
    prenom = input("Entrez le prenom  : ")
    nom = input("Entrez le nom  : ")
    note = input("Entrez le note : ")
    File.write(newID + "," + prenom + "," + nom + "," + note + "\n")
    print("La saisie des attribues secssefull ! ")
File.seek(0)
for line in File:
    print(line.strip())


File.close()