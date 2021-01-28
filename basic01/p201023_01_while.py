#반복문(while)
#조건이 참일동안 수행
# while True:
#     print('python!!!')

# a = 0
# while a < 10:
#     a += 1
#     print(a)

# a = 0
# while True:
#     a += 1
#     if a > 10: break
#     print(a)

#1부터 1씩증가하는 숫자의 합이 1000초과시 숫자 출력
#1)
# a = 0 #1씩 증가하는 수
# s = 0 #합계를 저장할 변수
# while True:
#     a += 1
#     s += a
#     if s>1000: break
#
# print('누적값:' , s)
# print('마지막숫자:', a)

#2)
# a = 0 #1씩 증가하는 수
# s = 0 #합계를 저장할 변수
# while s <= 1000:
#     a += 1
#     s += a
#
# print('누적값:' , s)
# print('마지막숫자:', a)

#실습)사용자에게 숫자를 계속 입력을 받아서 출력
#사용자가 0을 입력하면 반복문 종료
#1)
# while True:
#     num = int(input('숫자는?'))
#     if num == 0: break
#     print('입력숫자:', num)
#2)
# num = 1
# while num != 0:
#     num = int(input('숫자는?'))
#     print('입력숫자:', num)

#입력한 숫자를 더해서 합계를 출력하는 프로그램
#사용자가 q을 입력하면 반복문 종료
# s=0
# while True:
#     num = input('숫자는(q:종료)?')
#     if num=='q': break
#     s += int(num)
#
# print('누적합계:', s)
#실습)계산기 프로그램
#1)
# while True:
#     a = input('first:')
#     if a=='q': break
#     b = input('second:')
#     sign = input('sign:')
#     a=int(a); b=int(b)
#     if sign == '+':
#         print('더하기:', a+b)
#     elif sign == '-':
#         print('빼기:', a - b)
#     elif sign == '*':
#         print('곱하기:', a * b)
#     elif sign == '/':
#         print('나누기:', a / b)
#     else:
#         print('잘못된 기호')
#2)
# while True:
#     cal = input('계산식은?').split()
#     # print(cal)
#     if cal[0]=='q': break
#     a,sign,b = cal #언패킹
#     a=int(a); b= int(b)
#     if sign == '+':
#         print('더하기:', a+b)
#     elif sign == '-':
#         print('빼기:', a - b)
#     elif sign == '*':
#         print('곱하기:', a * b)
#     elif sign == '/':
#         print('나누기:', a / b)
#     else:
#         print('잘못된 기호')

#실습)가장 큰수 찾기
# data=[5,6,2,8,9,1]
# max = data[0]
# for x in data:
#     if x > max:
#         max = x
# print(max)

#실습)가장 작은수 찾기
data=[5,6,2,8,9,1]
min = data[0]
for x in data:
    if x < min:
        min = x
print(min)


















