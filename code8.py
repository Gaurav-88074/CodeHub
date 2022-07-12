
from code9 import insertDataIntoTextFiles

dummy_data = [
    ["title1", ["heading1.1","heading1.2"],["paragraph1.1","paragraph1.2"]],

    ["title2", ["heading2.1","heading2.2"],["paragraph2.1","paragraph2.2"]],

    ["title3", ["heading3.1","heading3.2"],["paragraph3.1","paragraph3.2"]],  
]

for index in range(0,len(dummy_data)):
    obj = dummy_data[index]
    insertDataIntoTextFiles(index,obj)




