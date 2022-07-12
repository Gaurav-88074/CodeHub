class pichlaJanam1():
    def getName(self):
        return "1"
class pichlaJanam2():
    def getName(self):
        return "2"
class student(pichlaJanam2,pichlaJanam1):
    def __init__(self):
        self.name = None
        self.age  = None
    def setData(self,name="Gaurav",age=12):
        self.name = name
        self.age = age
    def getData(self):
        return str(self.name)+" : "+str(self.age)

student1 = student()

print(student1.getName())

# student1.setData()
# print(student1.getData())