def force_sort(seq):
    ant_seq = []
    for i in seq:
        ant_seq.append(i)
    for i in range(len(seq)-1):
        if seq[i] > seq[i+1]:
            seq[i], seq[i+1] = seq[i], seq[i]
    dif = []
    for i in range(len(seq)):
        valor = seq[i] - ant_seq[i] 
        dif.append(valor)
    # print(seq)
    # print(dif)
    return dif


seq = [1, 3, 5, 4, 9]
assert force_sort(seq) == [0, 0, 0, 1, 0]
assert seq == [1, 3, 5, 5, 9]
   
seq = [1, 3, 5, 4, 9, 2, 15]
assert force_sort(seq) == [0, 0, 0, 1, 0, 7, 0]
assert seq == [1, 3, 5, 5, 9, 9, 15]
