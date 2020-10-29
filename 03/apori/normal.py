def ini(dataset,support):
    new = []
    count = [0 for i in range(70000)]

    for i in dataset:
        for j in i:
            # print(j)
            count[j-1] += 1

    for j in range(len(count)):
        if count[j] >= support:
            new.append([j+1])

    return new

def join(old):
    new = []
    ol=len(old)
    for i in range(ol):
        for j in range(i+1, ol):
            if old[i][:-1] == old[j][:-1]:
                if old[i][-1] != old[j][-1]:
                    temp = old[i][:-1]
                    temp.append(min(old[i][-1], old[j][-1]))
                    temp.append(max(old[i][-1], old[j][-1]))
                    if temp not in new:
                        new.append(temp)  
    
    final=[]
    for i in new:
        flag=1
        for j in i:
            temp=i.copy()
            temp.remove(j)
            if temp not in old:
                flag=0
                break
        if flag == 1:
            final.append(i)
    return final


def ins(a,b):
    flag=1

    for i in a:
        if i not in b:
            flag=0
            break
    
    return flag

def prune(dataset,old,support):
    count = [0 for i in range(len(old))]

    c=0
    for i in dataset:
        c+=1
        # print(c)
        for j in range(len(old)):
            if ins(old[j],i):
                count[j] += 1

    new = []
    for j in range(len(old)):
        if count[j] >= support:
            new.append(old[j])

    # print(len(new))
    return new