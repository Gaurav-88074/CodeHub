file  = open("1.txt","r")
data = file.read()
data = data.split("\n")
t=[]
for i in data:
    t.append("<"+i+">")
print(t)