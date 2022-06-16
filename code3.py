line1 = list(map(int,input().split(" ")))
line2 = list(map(int,input().split(" ")))

min = line1[1]+line2[1]
v = min%60
carry = (min-v)//60

hrs = line1[0]+line2[0]
hrs+=carry

print(hrs,v)