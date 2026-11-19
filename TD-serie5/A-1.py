File = open("notes.txt" , "r")
File.seek(0)
MyList = File.readlines()

Notes = []
for i in MyList:
    note = float(i)
    Notes.append(note)

moyenne = sum(Notes) / len(Notes)
print("La moyenne des notes est :" , moyenne)


File.close()

