import itertools 
from itertools import combinations


def sortarr(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [3,5,2,7,4,2,3] 
lst=[] 
blst = []
  
  
def sum_list(arr,total, a): 
    h=[] 
    c= arr 
    h=[combo for combo in combinations(c, a) if sum(combo) == total] 
    return h 

def remEM(klst):
    list2 = [e for e in klst if e]
    return list2
    

def rem_dup(test_list): 
    res = [] 
    for i in test_list: 
        if i not in res: 
            res.append(i) 
    return res 
  
def rem_na(lsk):
    resk = []
    for i in lsk:
        if i == 'na':
            continue
        else:
            resk.append(i)
    return resk
def Get_inp(): 
    i =0 
    while i < 7: 
        temp =int(input("Enter a no :")) 
        arr.append(temp) 
        i=i+1 
    
def sumOfOne():
    kblst = []
    j = 0
    print("\n\nThe Sum oF One : ")
    tkval = int(input("Enter A No to find : "))
    while j < len(arr):
        kblst.append(sum_list(arr,tkval,j))
        j = j + 1 
    j = 0
    res = [ele for ele in kblst if ele != []]
    merged = list(itertools.chain.from_iterable(res))
    print(tkval,":",merged)
    kblst.clear()

def sumOfAll(nlst):
    i = 0 
    j = 0
    print("\n\nThe Sum oF All : ")
    while i < len(nlst):
        while j < len(arr):
            # print(arr,nlst[i],j)
            blst.append(sum_list(arr,nlst[i],j))
            j = j + 1 
        # print("The Value of I %d"%i)
        j = 0
        res = [ele for ele in blst if ele != []]
        merged = list(itertools.chain.from_iterable(res))
        print(nlst[i],":",merged)
        i = i + 1
        blst.clear()

def validSum():      
    lst=list(itertools.chain.from_iterable(mat)) 
    nlst = rem_na(lst)
    tmplskt = sortarr(nlst)
    print("\nThe valid Sum is : ", tmplskt) 
    nlst = tmplskt
    nlst = rem_dup(nlst) 
    sumOfAll(nlst)
  
mat=[ 
     [21,"na","na","na",12], 
     ["na","na",12,"na","na"], 
     ["na","na","na","na","na"], 
     [17,"na","na","na","na"], 
     ["na",22,"na","na","na"], 
] 
  
validSum()
sumOfOne()
