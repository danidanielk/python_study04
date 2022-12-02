class Avengers:
    def __init__(self,name,age):
        print("Avengers Assemble")
        self.name=name
        self.age=age
        
    def attack(self):
        print("공격")
    
    def printInfo(self):
        print(self.name)
        print(self.age)
        

#오버로딩: 메소드명은같게 파라미터를 다르게 = 파이썬에 없음
#오버라이딩: 상속받은 메소드 기능에 뭘더 추가해서 재사용 = 파이썬에서 가능
class Ironman(Avengers):
    def __init__(self,name,age,suitType):
        Avengers.__init__(self, name, age)
        self.suitType=suitType
    def attack(self):
        Avengers.attack(self)
        print("액션빔~")
    def printInfo(self):
        Avengers.printInfo(self)
        print(self.suitType)
        
        
if __name__ == "__main__":
    i=Ironman("토니",1,"mk50")
    i.attack()
    i.printInfo()
    print("-----")
    
    
    
class hulk(Avengers):
    def __init__ (self,name,age,pantsSize):
        Avengers.__init__(self, name, age)
        self.pantsSize=pantsSize
    def attack(self):
        Avengers.attack(self)
        print("망치 주먹 뚜까 패기")
    def printInfo(self):
        Avengers.printInfo(self)
        print(self.pantsSize)

if __name__ ==("__main__"):
    h=hulk("헐크",23,"28")
    h.attack()
    h.printInfo()