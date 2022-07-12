def insertDataIntoTextFiles(index,row):
    sep = "====="
    fileName = str(index+1)+".txt"
    file = open(fileName,"w")
    #=====
    file.write(row[0]+"\n")

    file.write(sep+"\n")

    for heading in row[1]:
        file.write(heading+"\n")

    file.write(sep+"\n")

    for paragraph in row[2]:
        file.write(paragraph+"\n")
    file.close()
