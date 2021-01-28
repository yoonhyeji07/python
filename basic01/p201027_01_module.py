#모듈 사용하기
#현재시간 표현하기
# import time
# t = list(time.localtime())
# print(t)
# print(t[0],'년',t[1],'월',t[2],'일')
# t = time.localtime()
#
# import datetime
# print(datetime.datetime.now())
#
# print(time.time())

#프로그램 실행시간 지연
# import time
# print('시작')
# time.sleep(3)
# print('3초 지남')

#실습)
import p201026_01_function
import time
sec = p201026_01_function.inputDigital('초?')
print('시작')
for x in range(1,sec+1):
    print(x,'초')
    time.sleep(1)
print('끝')

#칼렌타 모듈 추가
# import calendar
# # calendar.prcal(3000)
# calendar.prmonth(2020,10)

#랜덤 모듈
import random
#0 <= 난수 < 1
# print(random.random())
#실습)주사위 게임
# 1) 5게임 실행
# aw=0; bw=0 #이긴 횟수
# for x in range(5):
#     a = random.randint(1,6)
#     b = random.randint(1,6)
#     print('A:', a, end=' ')
#     print('B:', b)
#     if a>b:
#         print('A승')
#         aw+=1
#     elif b>a:
#         print('B승')
#         bw+=1
#     else:
#         print('무승부')
#     print('-'*15)
#
# #최종결과
# print('A의승:', aw)
# print('B의승:', bw)
# if aw>bw:
#     print('A의 최종승')
# elif bw>aw:
#     print('B의 최종승')
# else:
#     print('최종 무승부')
# 2)3승이 먼저 되면 종료
# import random
# aw=0; bw=0
# while aw<3 and bw<3:
#     a = random.randint(1,6)
#     b = random.randint(1,6)
#     print(a,':',b)
#     if a>b:
#         print('A승')
#         aw+=1
#     elif b>a:
#         print('B승')
#         bw+=1
#     else:
#         print('무승부')
#     print('-'*10)
#     #만약에 aw가 3이상이거나
#     #bw가 3이상이면 반복문 탈출
#     # if aw>=3 or bw>=3:
#     #     break
#
# #최종결과
# print('A의승:', aw)
# print('B의승:', bw)
# if aw>bw:
#     print('A의 최종승')
# elif bw>aw:
#     print('B의 최종승')
# else:
#     print('최종 무승부')

#랜덤의 섞기
# import random
# data = ['해','해','달','달']
# random.shuffle(data)
# print(data)

#가위/바위/보 게임
# import random
# a = random.choice(['가위','바위','보'])
# b = random.choice(['가위','바위','보'])
# print('A:', a, 'B:', b)
# if a==b:
#     print('무승부')
# elif a=='가위' and b=='바위':
#     print('B승')
# elif a=='가위' and b=='보':
#     print('A승')
# elif a=='바위' and b=='가위':
#     print('A승')
# elif a=='바위' and b=='보':
#     print('B승')
# elif a=='보' and b=='가위':
#     print('B승')
# elif a=='보' and b=='바위':
#     print('A승')

#딕셔너리로 표현한다면
# import random as r #알리어스명
# d ={'가위바위':'B','가위보':'A',
#     '바위가위':'A','바위보':'B',
#     '보가위':'B','보바위':'A'}
# a = r.choice(['가위','바위','보'])
# b = r.choice(['가위','바위','보'])
# print('A:', a, 'B:', b)
# if a==b:
#     print('무승부')
# else:
#     print(d[a+b],'승')

#랜덤으로 데이터 고르기
from random import sample
lotto = sample(range(1,46),6)
print(lotto)
# lotto.sort()
# print(lotto)
print(sorted(lotto))
print(lotto)
#사용자에게 로또 번호를 입력받아 맞은갯수 출력
lotto = input('로또번호는?').split(',')
print(lotto)
right = 0 #맞은갯수

















