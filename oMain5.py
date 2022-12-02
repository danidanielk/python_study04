#다중상속~!




class Avengers:
    def __init__(self,realName):
        self.realName=realName
    def attack(self):
        print("머찐 공격!")
    def printInfo(self):
        print(self.realName)
        
        
class Human:
    def __init__(self,age):
        self.age=age
        
    def eat(self):
        print("잘먹음")
    def attack(self):
        print("잘때림")
    def printInfo(self):
        print(self.age)
        
#파이썬은 다중상속 가능
class Ironman(Avengers,Human):
    def __init__(self,realName,age):
        Avengers.__init__(self, realName)
        Human.__init__(self, age)
    
    def attack(self):
        Avengers.attack(self)
        Human.attack(self)
        print("두개 다가능")
    def printInfo(self):
        Avengers.printInfo(self)
        Human.printInfo(self)
    def eat(self):
        Human.eat(self)
        
if __name__ ==("__main__"):
    i=Ironman("다니엘",40)
    i.attack()
    i.printInfo()
    i.eat()