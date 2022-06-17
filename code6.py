def compute(array):
    array.sort()
    for i in range(1,len(array)+1):
        if array[i-1]!=i:
            return [array[i-1],i]
    return []
array = [3,1,2,5,3]
print(compute(array))
            