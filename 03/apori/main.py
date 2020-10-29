import csv
from opt3 import *
from normal import *
from opt2 import *
import time


def run_original(dataset,support,k):
    ans=[]
    al = ini(dataset,support) #Initialisation 

    for i in range(k): 
        if al == []:
            break
        for i in al:
            ans.append(i)
        al = join(al)
        al = prune(dataset,al,support)
    
    return len(ans)



def run_reduction(dataset,support,k):
    ans=[]
    al = ini(dataset,support)                                                        #Initialisation for first and second
    isValid = [1 for i in range(len(dataset))]

    for i in range(k):                                                #Second Optimization
        if al == []:
            break
        for i in al:
            ans.append(i)
        al = join(al)
        al,isValid = opt2(dataset,isValid,al,support)

    return len(ans)




def run_hash(dataset,support,k):
    has = dict()
    ans=[]
    al,has = opt3ini(dataset,has,k,support)                                                    #initialization for first
    
    for i in range(k):                                                #Third Optimization
        if al == []:
            break
        for i in al:
            ans.append(i)
        al = join(al)
        if k==2:
            al = pruneFromHash(has,al,support)
        else:
            al = prune(dataset,al,support)

    return len(ans)


def read_file(filename):
    dataset = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            dataset.append(sorted([int(i) for i in row[0].split('-1')[:-1]]))

    return dataset

def main():
    dataset=read_file('LEVI.txt')
    support = 400
    k = 10
    print('run_original')
    start = time.time()
    print(run_original(dataset,support,k))
    end = time.time()
    print(end - start)
    print('run_reduction')
    start = time.time()
    print(run_reduction(dataset,support,k))
    end = time.time()
    print(end - start)
    print('run_hash')
    start = time.time()
    print(run_hash(dataset,support,k))
    end = time.time()
    print(end - start)




if __name__=="__main__":
    main()