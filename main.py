from __future__ import print_function
import itertools 
from itertools import combinations 

arr = [2,3,4,5,6,7,8] 
  
  
def sum_list(arr,total, a): 
    h= [] 
    c= arr 
    h=[combo for combo in combinations(c, a) if sum(combo) == total] 
    return h 

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
  
mat=[ 
     [21,"na","na","na",12], 
     ["na","na",12,"na","na"], 
     ["na","na","na","na","na"], 
     [17,"na","na","na","na"], 
     ["na",22,"na","na","na"], 
] 
  
lst=[] 

lst=list(itertools.chain.from_iterable(mat)) 
 
 #print(lst) 
nlst = rem_dup(lst) 
nlst.remove('na') 
print("The Nlst value is ") 
print(nlst) 



tdic = {}

blst = []
i = 0 
j = 0
while i < len(nlst):
    while j < len(arr):
        # print(arr,nlst[i],j)
        blst.append(sum_list(arr,nlst[i],j))
        j = j + 1 
    # print("The Value of I %d"%i)
    j = 0
    tdic = {nlst[i]:blst}
    print(tdic)
    i = i + 1
    blst.clear()


print(tdic)