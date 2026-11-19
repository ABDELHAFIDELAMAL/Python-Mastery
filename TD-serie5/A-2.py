File1 = open("notes.txt", "r")
File2 = open("notes2.txt", "a+")

File1.seek(0)
MyList = File1.readlines()

for i in MyList:
    note = float(i.strip()) # remove newline

    if note < 10:
        File2.write(str(note) + " recale\n")
    else:
        File2.write(str(note) + " admis\n")

File1.close()
File2.close()
