
class wildanimal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)
        



if __name__=="__main__":
# 위  if __name__=="__main__": 의 의미는 이 모듈을 실행했을 ㄸ ㅐ동작해라.
# 프로그램의 시작점. 이 모듈이 임포트 당했을 때 아무작업도 하지말고
# 실제 이 모듈에서 코드가 실행 되었을 때만 동작해라.
    from animal.pet import dog
    d=dog("냥냥이",33)
    d.printInfo()