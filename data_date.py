# 날짜처리.
#아래하이픈 없는 두번째 것으로 임포트.
from datetime import datetime


#현재시간 날짜 
now= datetime.today()
print(now)

#특정 시간 날짜
yesterday= datetime(2022,11,9)
print(yesterday)
print(yesterday.year)
print(yesterday.month)
print(yesterday.day)

#생일을 입력받아서 나이를 계산해주는 프로그램.
birthday=input("yyyy/mm/dd : ")
year = now.year
print(year-int(birthday[0:4])+1)

#문자열을 datetime 으로 바꾸는법 = strptime
bd=datetime.strptime(birthday,"%Y/%m/%d")
print(bd)
#datetime을 문자열로 바꾸는법= strftime
bd2=datetime.strftime(bd,"%A")
print(bd2)


#test 특정날짜를 연/월/일 형태로 입력받아서 -> 일/월 형태의 문자열로 출력하시오.
day=input("연/월/일: [입력]")
day2 = datetime.strptime(day,"%Y/%m/%d")
day3 = datetime.strftime(day2,"%d/%m")
print(day3)
print(type(day3))

