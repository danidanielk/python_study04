

#클래스 불러오기 1번째 방법
import animal.pet
#패키지명.모듈명.클래스명
d=animal.pet.dog("쪼ㄱ꼬",3)
d.printInfo()



#클래스 불러오기 2번째 방법
import animal.pet as pp
#임포트한 패키지명.모듈명 에 별칭붙여다 갔다쓰기
d=pp.dog("쪼옦꼬오",5)
d.printInfo()


#클래스 불러오기 3번째 방법 나는 이걸로 선택..
from animal.pet import dog
d=dog("냥이",55)
d.printInfo()