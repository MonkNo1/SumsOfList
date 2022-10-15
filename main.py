import itertools 
from itertools import combinations
from arrSort import sortarr


arr = [3,5,2,7,4,2,3] 
  
  
def sum_list(arr,total, a): 
    h= [] 
    c= arr 
    h=[combo for combo in combinations(c, a) if sum(combo) == total] 
    return h 

  
# def remEM(klst):
#     print("Remove MT List : ")
#     i = 0
#     while i < len(klst):
#         print(len(klst[i]))
#         if len(klst[i]) == 0:
#             klst.pop(i)
#         i = i + 1   
#     return klst
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
tmplskt = sortarr(nlst)
print("The Nlst value is ") 
print(tmplskt) 
nlst = tmplskt



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
    print(nlst[i])
    print(blst)
    i = i + 1
    blst.clear()


print(tdic)