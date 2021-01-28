#함수(내장함수)
# data =[5,6,9,2,1]
# print(max(data))
# print(min(data))
# print(sum(data))
# print(sum(data)/len(data))

#문자=>코드값
# print(ord('A'))
# print(ord('홍'))
# print(ord('김'))
# #코드=>문자
# print(chr(65))
# print(chr(44608))

#이진수를 10진수로
# 8bit (1byte)
# 00000000~11111111 => 0 ~ 255

#10진법=>2진법
# print(bin(255))
#10진법=>8진법
# print(oct(255))
#10진법=>16진법
# print(hex(255))

#사용자함수 만들기
#반환값이 없는 함수
# def printName(name,age):
#     print(name, age)
#
# printName('홍길동',20)
# printName('이순신',45)

#반환값이 있는 함수
#지역변수 : 함수안에서 생성된 변수
#합(add)
# def add(a,b): #지역변수(매개변수)
#     c=a+b
#     return c
# #차(sub)
# def sub(a,b):
#     return a-b
# #곱(mul)
# def mul(a,b):
#     return a*b
# #나누기(div)
# def div(a,b):
#     return a/b
#
# a=30; b=20 #전역변수
# s = add(a,b)
# print('더하기:', s)
# print('빼기:', sub(a,b))
# print('곱하기:', mul(a,b))
# print('나누기:', div(a,b))
# print(a)

#함수에서 전역변수 사용
# a=100
# def cal():
#     global a #전역변수 a
#     print(a+10)
# cal()

#두수를 매개변수로 받아서 사칙연산을 return
# def cal(a,b):
#     return a+b,a-b,a*b,a/b
#
# a,b,c,d=cal(30,20)
# print('더하기:', a)
# print('빼기:', b)
# print('곱하기:', c)
# print('나누기:', d)

#실습)구구단 출력함수
# def gugudan(dan):
#     for x in range(1,10):
#         print(dan,'*',x,'=', dan*x)
#
# d = int(input('단수는?'))
# gugudan(d)

# #실습)매개변수(리스트)의 값을 더하는 함수
# def sum(data):
#     s = 0
#     for x in data:
#         s = s+x
#
#     return s #합계를 반환
#
# data=[4,10,25,7,8,1]
# print(sum(data))

#실습)팩토리얼 구하고 반환하는 함수
# def factory(n):
#     m=1
#     for x in range(1,n+1):
#         m *= x
#     return m
#
# print(factory(5))

#실습)원의 넓이를 구하여 반환하는 함수
# 함수명 : circleArea
# 매개변수 : 반지름(r)
# 반환값 : 원의 넓이(r*r*3.14)
# def circleArea(r):
#     return r*r*3.14
#
# print(circleArea(7.5))

#함수의 장점 : 재활용성,유지보수
#실습)사용자에게 정수를 입력받아
# 입력받은 값을 반환하는 함수
# 함수명 : inputDigital
# 매개변수 : 없음
# 반환값 : 입력받은 정수
# def inputDigital(msg):
#     while True:
#         a = input(msg)
#         if a.isdigit():
#             return int(a)
#
# a=inputDigital('첫번째정수?')
# b=inputDigital('두번째정수?')
# print(a+b)

#실습)두수와 기호를 사용자에게 입력받아
#사칙연산을 하는 프로그램(함수사용)
#사용자입력함수:inputDigital(msg)
#기호입력함수 : inputSign
#사칙연산함수 : add, sub, mul, div
# def inputDigital(msg):
#     while True:
#         a = input(msg)
#         if a.isdigit():
#             return int(a)
#
# def inputSign():
#     sign = ['+','-','*','/']
#     while True:
#         a = input('기호?')
#         if a in sign:
#             return a
# 합(add)
# def add(a,b): #지역변수(매개변수)
#     return a+b
# #차(sub)
# def sub(a,b):
#     return a-b
# #곱(mul)
# def mul(a,b):
#     return a*b
# #나누기(div)
# def div(a,b):
#     return a/b

#사용자가 첫번째 정수에 0을 입력 종료
# while True:
#     print('-'*20)
#     a=inputDigital('첫번째정수?')
#     if a==0:
#         print('종료')
#         break
#     b=inputDigital('두번째정수?')
#     sign = inputSign()
#     if sign=='+':
#         print('더하기:', add(a,b))
#     elif sign =='-':
#         print('빼기:', sub(a, b))
#     elif sign == '*':
#         print('곱하기:', mul(a, b))
#     elif sign == '/':
#         print('나누기:', div(a, b))
#     else:
#         print('잘못된 연산')

#재귀함수
# 자기자신을 호출하는 함수
def test(n):
    if n>2 : return
    print(n)
    test(n+1)

test(0)















