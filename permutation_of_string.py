def permutation_of_string(st,cur):

    if len(st) == 0:
        print(cur)
        return
    for i in range(len(st)):
        ch = st[i]
        ls = st[0:i]
        rs = st[i+1:]
        fs = ls+rs
        permutation_of_string(fs,cur+ch)











st = "abc"
cur = " "
permutation_of_string(st,cur)