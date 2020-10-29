import csv
dataset = []
with open('SIGN.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        dataset.append(sorted([int(i) for i in row[0].split('-1')[:-1]]))
support = 400

def join(old):
    new = []
    for i in range(len(old)):
        for j in range(i+1, len(old)):
            if old[i][:-1] == old[j][:-1] and old[i][-1] != old[j][-1]:
                temp = old[i][:-1]
                temp.append(min(old[i][-1], old[j][-1]))
                temp.append(max(old[i][-1], old[j][-1]))
                if temp not in new:
                    new.append(temp)  
    final=[]
    # print(new)
    for i in new:
        # if len(i) ==2:
        #     final=new
        #     break
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

def prune(old):
    global dataset
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


k = 10


def ini():
    global dataset
    global support
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


isValid = [1 for i in range(len(dataset))]


def opt2(old):
    global dataset
    global isValid
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

    return new


has = dict()


def opt3ini():
    global dataset
    global has
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

    return new

def pruneFromHash(old):
    global has
    new=[]

    for i in old:
        # if has[(i[0]*10000+i[1])%1000007] >= support:
        if has[(i[0],i[1])] >= support:
            new.append(i)
    
    return new

ans=[]
# al = ini()                                                        #Initialisation for first and second

# for i in range(k):                                                #Normal One 
#     print(len(al))
#     if al == []:
#         break
#     for i in al:
#         ans.append(i)
#     al = join(al)
#     al = prune(al)

# for i in range(k):                                                #Second Optimization
#     if al == []:
#         break
#     for i in al:
#         ans.append(i)
#     al = join(al)
#     al = opt2(al)

al = opt3ini()                                                    #initialization for first
for i in range(k):                                                #Third Optimization
    if al == []:
        break
    for i in al:
        ans.append(i)
    al = join(al)
    if k==2:
        al = pruneFromHash(al)
    else:
        al = prune(al)

print(len(ans))
