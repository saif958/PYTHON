class emp:
    def __init__(self,name):
        self.name= name
        print(name)
class student(emp):
    pass
emp1 = emp("doe")
std1 = student("doe","19")
