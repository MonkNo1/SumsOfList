import itertools

arr = []

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

nlst = rem_dup(lst)
nlst.remove('na')
print("The Nlst value is ")
print(nlst.sort())

# dic = {}
