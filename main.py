import itertools

arr = [2,3,4,5,6,7,8]


def find_sum(inp,t):
    i = 0
    tsl = []
    tlst = []
    while i < len(inp):
        if (i+1) > len(inp):
            break
        ts = inp[i] + inp[(i + 1)]
        if ts == t : 
           tsl.append(i) 
           tsl.append(i+1) 
        tlst.append(tsl)
        i = i + 1
    #test for adding 3 nos 
    i = 0 
    while i < len(inp):
        if (i+1) > len(inp) or (i+2) > len(inp)  :
            break
        ts = inp[i] + inp[(i + 1)]+inp[(i + 2)]
        if ts == t : 
           tsl.append(i) 
           tsl.append(i+1)
           tsl.append(i+2)
        tlst.append(tsl)
    i = 0 
    while i < len(inp):
        if (i+1) > len(inp) or (i+2) > len(inp)  or (i+3) > len(inp) :
            break
        ts = inp[i] + inp[(i + 1)]+inp[(i + 2)]+inp[(i+3)]
        if ts == t : 
           tsl.append(i) 
           tsl.append(i+1)
           tsl.append(i+2)
           tsl.append(i+3)
        tlst.append(tsl)
    
    return tlst

def rem_dup(test_list):
    res = []
    for i in test_list:
        if i not in res:
            res.append(i)
    return res

def Get_inp():
    i = 0
    while i < 7:
        temp = int(input("Enter a no :"))
        arr.append(temp)
        i = i +1

mat = [
    [21,"na","na","na",12],
    ["na","na",12,"na","na"],
    ["na","na","na","na","na"],
    [17,"na","na","na","na"],
    ["na",22,"na","na","na"],
]

lst = []


lst = list(itertools.chain.from_iterable(mat))

# print(lst)
nlst = rem_dup(lst)
nlst.remove('na')
print("The Nlst value is ")
print(nlst)

# dic = {}
