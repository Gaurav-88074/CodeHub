
def eliminater(string):
    if len(string)==0:
        return False
    else:
        return True
#''
def fetchDataFromFile(fileName):
    file = open(fileName,"r")
    fileData = file.read().split("=====")

    title = fileData[0].split("\n")
    title = list(filter(eliminater,title))[0]#optional;  

    heading = fileData[1].split("\n")
    heading = list(filter(eliminater,heading))  

    paragraph = fileData[2].split("\n")
    paragraph =list(filter(eliminater,paragraph)) 

    res = [
        title,
        heading,
        paragraph
    ]
    file.close()
    return res
row = fetchDataFromFile("1.txt")

print(row)
