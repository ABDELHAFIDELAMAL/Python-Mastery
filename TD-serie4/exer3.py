notes = [12 , 7 , 15 , 9, 20 , 11]

moyenne = sum(notes) / len(notes)
meilleure = max(notes)

les_notes = []
for note in notes:
    if note >= 10 :
        les_notes.append(note)

print(f"moyenne : {moyenne:.2f}\n la meilleure : {meilleure}\n les notes > 10 est : {les_notes} \n {les_notes[::-1]}")

new_notes = [note for note in notes if note >= 10]
print("new notes = " , new_notes)