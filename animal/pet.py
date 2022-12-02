
class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def printInfo(self):
        print(self.name,self.age)
        
        
if __name__("__main__"):
    from animal.wild import wildanimal
    w=wildanimal("늑대",3333333)
    w.info()

