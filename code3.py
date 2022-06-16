
line1 = list(map(int,input().split(" ")))
line2 = list(map(int,input().split(" ")))

min = line1[1]+line2[1]
v = min%60
carry = (min-v)//60

hrs = line1[0]+line2[0]
hrs%=24

hrs+=carry

a = hrs
b = v
if(hrs<10):
    a = "0"+str(a)
if(v<10):
    b = "0"+str(v)

print(a,b)
