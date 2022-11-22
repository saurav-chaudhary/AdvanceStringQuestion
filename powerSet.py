def powerSet(st,i,cur):

    if i == len(st):
        print(cur)
        return
    powerSet(st,i+1,cur+st[i])
    powerSet(st,i+1,cur)







st = "abc"

cur = ""
i = 0
powerSet(st,i,cur)
