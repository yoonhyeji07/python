#조건(if)
# a = 10
# if a > 0:
#     print('양수')
#     print('0보다 큰수')
# else:
#     print('음수')
#     print('0보다 작은수')

#등급매기기 :  60점 이상이면 pass 아니면 fail
# s = int(input('점수는?'))
# if s >= 60:
#     print('pass')
# else:
#     print('fail')

#여러개의 조건
# a=0
# if a>0:
#     print('양수')
# elif a<0:
#     print('음수')
# else:
#     print('음수도 양수도 아님')

#A(~90) , B(89~80), C(79~70), D(69~60), F(59~0)
# a=85
# if a>=90:
#     print('A')
# elif a>=80:
#     print('B')
# elif a>=70:
#     print('C')
# elif a>=60:
#     print('D')
# else:
#     print('F')
#
# print('성적계산완료')

#실습) 짝홀수 판별
# a = 10
# print(a%2==0)
# if a%2==0:
#     print('짝수')
# else:
#     print('홀수')

#실습)두수중 큰수 출력하기
# a = int(input('첫번째수?'))
# b = int(input('두번째수?'))
# if a>b:
#     print('a의 값이 더크다', a)
# elif b>a:
#     print('b의 값이 더크다',b)
# else:
#     print('두같은 같다')

#중첩 if문으로(elif 방법으로 해결하자)
# a = int(input('첫번째수?'))
# b = int(input('두번째수?'))
#
# if a>b:
#     print(a)
# else:
#     if b>a:
#         print(b)
#     else:
#         print('같다')

#실습)거스름돈 계산
# money = int(input('내신돈?'))
# amount = int(input('상품가격?'))
# if money > amount:
#     print('거스름돈:', money-amount)
# elif amount > money:
#     print('돈이 부족:', amount-money, '부족')
# else:
#     print('계산완료')

# 실습)태양계의 행성 여부 출력
# solarS = ['수성','금성','지구','화성','목성',
#           '토성','천왕성','해왕성','명왕성']
#
# earth = input('행성의 이름은?')
# if earth in solarS:
#     print(earth, '는 태양계의 행성',sep='')
# else:
#     print(earth, '는 태양계의 행성아님',sep='')

#논리연산자
# a=10; b=-5
# print(a>0 and b>0)
# print(a>0 or b>0)
# print(not a>0)

#두수가 0보다 크면 '둘다 양수' 출력
#두수가 0보다 작으면 '둘다 음수' 출력
#한수만 0보다 크면 '하나는 음수' 출력
# a =10; b=-20
# if a>0 and b>0:
#     print('둘다 양수')
# elif a<0 and b<0:
#     print('둘다 음수')
# else:
#     print('하나는 음수')

#다른 알고리즘
# a =10; b=-20
# if a > 0 or b > 0:
#     print('둘다 양수')
# elif a>0 or b>0  :
#     print('하나는 양수')
# else:
#     print('둘다 음수')

#실습)
# menu={1:['자장면',5000], 2:['짬뽕',6000],
#       3:['설렁탕',8000], 4:['비빔밥',6500],
#       5:['피자',9000],6:['스파게티',12000]}
# print('1.자장면,2.짬뽕,3.설렁탕,4.비빔밥,5.피자,6.스파게티:')
# no = int(input())
# #선택한메뉴 출력
# if no in menu.keys():
#     print(menu[no][0], '선택')
#     print(menu[no][1], '원')
#     if no in [1,2]:
#         print('중식코너로 가세요')
#     elif no in [3,4]:
#         print('한식코너로 가세요')
#     elif no in [5,6]:
#         print('양식코너로 가세요')
# else:
#     print('없는 메뉴입니다.')

#코너가 확장되더라도 소스 수정없이 바꾼다면
# menu={1:['자장면',5000,'중식'], 2:['짬뽕',6000,'중식'],
#       3:['설렁탕',8000,'한식'], 4:['비빔밥',6500,'한식'],
#       5:['피자',9000,'양식'],6:['스파게티',12000,'양식']}
# print(1,menu[1][0])
# print(2,menu[2][0])
# print(3,menu[3][0])
# print(4,menu[4][0])
# print(5,menu[5][0])
# print(6,menu[6][0])
# print('-'*10)
# no = int(input('메뉴:'))
# print('-'*10)
# #선택한메뉴 출력
# if no in menu.keys(): #선택한 키 포함여부
#     print(menu[no][0], '선택')
#     print('가격은 %d원 입니다'%(menu[no][1]))
# else:
#     print('없는 메뉴입니다.')

#실습)적정체중 구하기
height = int(input('키는?')) #키
weight = int(input('몸무게는?')) #몸무게

normal = (height-100) * 0.9 #정상몸무게
print('적정체중:', normal)
if weight < normal*0.9:
    print('저체중')
elif weight <= normal * 1.1:
    print('정상체중')
else:
    print('과체중')










