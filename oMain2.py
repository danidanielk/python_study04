#생성자 : 객체가 메모리상에 만들어질때 호출하는 메소드
#        파이썬은 overloading이 안되니 ->생성자를 하나만.

class Book:
        
    def __init__(self,title,price):
        print("오버로딩 된 생성자")
        self.title=title
        self.price=price
        #보통 이렇게 생성자에서 멤버변수를 만들어서 결정한다.
    
    def printInfo(self):
        print(self.title,self.price)
        
#소멸자 : 객체가 메모리상에서 사라질 때 호출되는 메소드 (destructor)
    def __del__(self):
        print("책 삭제")
        
b1=Book("진격의 거인",50000)
b1.printInfo()


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def printInfo(self):
        print(self.name, self.age)
        
    def __del__(self):
        print("사람 소멸")
        
p=person("다니",50)
p.printInfo()    