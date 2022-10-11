import itertools
from itertools import combinations

arr = [2,3,4,5,6,7,8]


def sum_list(arr,total, a):
    h = []
    c = arr
    h = [combo for combo in combinations(c, a) if sum(combo) == total]
    return h


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


i = 1
for x in nlst:
    i = i + 1
    # print(i)
    # print(len(nlst))
    if i > (len(nlst)+1):
        break
    # print(x)
    kst = sum_list(arr,x,i)
    print(kst)

