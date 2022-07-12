from re import I


arr = [5,0,-1,0,1,2,-1]
res  = arr[0];
count= arr[0];
if count<0 : count = 0
for i in range(1,len(arr)):
    count+=arr[i];
    res = max(res,count)
    if count<0 : count = 0
print(res)