line1 = list(map(int,input().split(" ")))
line2 = list(map(int,input().split(" ")))

min = line1[1]+line2[1]
v = min%60
carry = (min-v)//60

hrs = line1[0]+line2[0]
hrs+=carry
if(hrs<10):
    print("0"+str(hrs),v)
else:
    print(hrs,v)