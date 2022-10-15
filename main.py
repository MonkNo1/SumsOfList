import itertools 
from itertools import combinations
from arrSort import sortarr


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
    print(tkval,":",kblst)
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
        print(nlst[i],":",blst)
        i = i + 1
        blst.clear()

def validSum():      
    lst=list(itertools.chain.from_iterable(mat)) 
    nlst = rem_dup(lst) 
    nlst.remove('na')
    tmplskt = sortarr(nlst)
    print("\nThe valid Sum is : ", tmplskt) 
    nlst = tmplskt
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
