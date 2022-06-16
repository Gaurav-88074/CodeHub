def compute(array,k):
    array.sort()
    res = 0
    for i in range(k):
        res+=array[i]
    return res
#---------------
n = int(input())
for i in range(n):
    k = int(input())
    size = int(input())
    array = list(map(int,input().split(" ")))
    print(compute(array,k))