from normal import *

def opt2(dataset,isValid,old,support):
    count = [0 for i in range(len(old))]

    for i in range(len(dataset)):
        if isValid[i] == 0:
            continue
        fl = 0
        for j in range(len(old)):
            if ins(old[j],dataset[i]):
                count[j] += 1
                fl = 1
        isValid[i] = fl

    new = []
    for j in range(len(old)):
        if count[j] >= support:
            new.append(old[j])

    return new,isValid
