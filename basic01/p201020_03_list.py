#리스트
# a = [10,20,30]
# print(a[0])
# print(a[:-1]) #마지막 데이터 제거

#a = [10,3.14,'hello', '$']
# print(a[2])
# print(a[2][1])
# print(a[2][2:-1])

#리스트 특징
#순서가 있다
#길이 변경 안됨
#중복값 허용

# 학생의 키,몸무게, 혈액형
# s = [['홍길동',160,55.5,'A'], ['이순신',175,80.2,'B']]
# print('이름:', s[0][0])
# print('키:', s[0][1])
# print('몸무게:', s[0][2])
# #이름변경
# s[0][4] ='100'
# print(s)

#리스트에 값추가
# . : 도트연산자를 이용한 메소드 접근
# a = [100, 200, 300]
# a.append(300) #메소드 : 리스트의 끝에 값 추가 기능
# print(a)
# print(a.count(300))
# a.remove(100)
# print(a)
# a.clear()
# print(a)

#실습)
# listX = ['blue','red','green','white','black']
# print(listX[2:])
# listX[2] = 'yellow'
# print(listX)

#실습)
s = input('문자열은?')
print(s.split(','))
















