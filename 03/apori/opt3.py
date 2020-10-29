def opt3ini(dataset,has,k,support):
    new = []
    count = [0 for i in range(70000)]

    for i in dataset:
        for j in range(len(i)):
            count[i[j]-1] += 1
            for k in range(j+1, len(i)):
                if (i[j],i[k]) not in has:
                    # has[(i[j]*10000+i[k]) % 1000007] = 1
                    has[(i[j],i[k])] = 1
                else:
                    # has[(i[j]*10000+i[k]) % 1000007] += 1
                    has[(i[j],i[k])] += 1

    for j in range(len(count)):
        if count[j] >= support:
            new.append([j+1])

    return new,has

def pruneFromHash(has,old,support):
    new=[]
    for i in old:
        # if has[(i[0]*10000+i[1])%1000007] >= support:
        if has[(i[0],i[1])] >= support:
            new.append(i)
    
    return new

