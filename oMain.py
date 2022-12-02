class Dog():
    def bark(self):
        print("월월")
    
    #변수넣을땐 self 로
    def info(self):
        self.name
        self.age
        print(self.name, self.age)
    @staticmethod
    def staticMethodTest():
        print("스테틱메쏘드입니다.")


d=Dog()
d.name="쪼꼬"
d.age=7

d.bark()
d.info()
d.staticMethodTest()

a=d.name
print(a)
b=d.age
print(b)