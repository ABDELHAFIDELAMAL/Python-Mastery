def sequ_comp(seq):
    newseq = ""
    for i in seq:

        if i == 'A':
            newseq += 'T'

        elif i == 'T':
            newseq += 'A'

        elif i == 'C':
            newseq += 'G'

        elif i == 'G':
            newseq += 'C'

    return newseq

seq = "ACTGCCCT"
print(sequ_comp(seq))
