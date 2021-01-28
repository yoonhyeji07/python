#반복문 : for
# for x in ['a','b','c']:
#     print(x)

# for x in 'hello':
#     print(x)

# for x in (1,2,3,4,5):
#     print(x, end=' ')
# print({1:'a',2:'b',3:'c'}.keys())
# print({1:'a',2:'b',3:'c'}.values())
# print({1:'a',2:'b',3:'c'}.items())

#언패킹
# for x,y in {1:'a',2:'b',3:'c'}.items():
#     print(x, y)

#정수리스트를 생성해주는 함수
# print(list(range(11))) #stop
# print(list(range(5,11))) #start,stop
# print(list(range(10,20,3))) #start,stop,step
# #5,4,3,2,1
# print(list(range(5,0,-1))) #start,stop,step

# for x in range(1,11):
#     print(x)

# a=[['홍길동',65],['이순신',55],['박자바',45]]
# # print(len(a))
#
# print('번호|  이름  | 몸무게')
# print('='*20)
# for x in range(len(a)): #[0,1,2]
#     print('%3d |%4s |%5d'%(x+1,a[x][0],a[x][1]))

#1~10까지의 합계구하기
# s=0 #초기화
# for x in range(1,11):
#     # print(x)
#     s += x #복합 연산자
# print('합계:', s)

#짝홀수 구분하기
# for x in range(0,11):
#     print(x,':',end='')
#     if x%2==0:
#         print('짝수')
#     else:
#         print('홀수')

#실습)합계가 100이 넘으면 때까지의 수
# s = 0
# for x in range(1,100):
#     s += x
#     if s > 100:
#         print('100이 넘는수 x:', x)
#         print('합계:', s)
#         break #반복문을 탈출
# else: #정상적인 수행(break를 만나지 않았을경우)
#     print('합계가 100을 넘지 못했다')

#실습)바른말 사용자
# wordL = ['안녕', '반가워', '고마워', '바보', '또만나']
# badWord = ['바보','멍청이','홍보']
# for x in wordL:
#     if x in badWord:
#         print('강퇴!')
#         break
# else: #break를 만나지 않았을때
#     print('바른말사용!')

#for의 else가 없다면
# badB = False #강퇴 대상자 여부
# wordL = ['안녕', '반가워', '고마워', '바보', '또만나']
# badWord = ['바보','멍청이','홍보']
# for x in wordL:
#     if x in badWord:
#         badB = True
#         print('강퇴!')
#         break
# #강퇴대상자가 아닐때만 출력
# if not badB: print('바른말사용!')

#continue
# for x in [80,65,55,44,90]:
#     if x<60: continue
#     print('%d점 합격'%x)

#continue없이
# for x in [80,65,55,44,90]:
#     if x>=60: print('%d점 합격'%x)
#break사용
# for x in [80,45,90,85,90]:
#     if x<60:
#         print('불합격!')
#         break
# else:
#     print('합격!')

#continue사용
# for x in [80,45,32,85,90]:
#     if x>=60:continue
#     print('불합격!')
#     break
# else:
#     print('합격!')

#실습)300점 이상이면 합격
# score = [100,100,100,69,45]
# score2 = [10,10,10,69,45]
#
# s = 0
# for x in score2:
#     s += x
#     if s>=300:
#         print('합격')
#         break
# else:
#     print('불합격')

#합계를 출력해야 하면
# score = [100,100,100,69,45]
# s=0
# for x in score:
#     s+=x
#
# if s>=300: print('합격!')
# else: print('불합격!')
#
# print('합계:', s)

#flag값(booean)으로 체크한다면
# score = [10,10,10,69,45]
# flag = False #합격여부
# s = 0
# for x in score:
#     s += x
#     if s>=300: flag=True
#
# #flag는 값이 True/False
# if not flag:
#     print('불합격')
# else:
#     print('합격')
# print(s)


#실습)구구단 출력
# dan = int(input('단수는?'))
# for x in range(1,10):
#     # print(4,'*',x, '=', 4*x)
#     print('%d * %d = %d'%(dan,x,dan*x))

#실습)3의배수
# no = int(input('마지막숫자?'))
# for x in range(0,no+1,3):
#     print(x)
#
# no = int(input('마지막숫자?'))
# for x in range(no+1):
#     if x%3 == 0:
#         print(x)

#실습)
# 별찍기1
# for x in range(1,7):
#     print('*' * x)

#별찍기2
# for x in range(6,0,-1):
#     print('*' * x)

#별찍기3) 과제
# su = int(input('몇줄?'))
# for x in range(1,su+1):
#     print(' '*(su-x),'*'*x,sep='')

#90점이상 학생 출력
# 1)
# dicA = {1:94, 2:87, 3:91, 4:75, 5:92}
# for x in dicA.items():
#     # print(x)
#     if x[1] >= 90:
#         print(x[0],'번')
# 2)
# dicA = {1:94, 2:87, 3:91, 4:75, 5:92}
# for no, score in dicA.items():
#     # print(no, score)
#     if score>90:
#         print(no,'번:', score)

#히스토그램 그리기
# listA = ['hong','lee','park']
# qty=[]
# #판매수량 입력
# # 홍길동의 판매수량은? 10
# for name in listA:
#     q = int(input('%5s 판매수량?'%name))
#     qty.append(q)
#
# # print(qty)
# #판매수량 출력
# for x in range(len(listA)):
#     print('%-5s:'%listA[x], '*' * qty[x])

#딕셔너리로 데이터 표현(과제)
# sales = {'홍길동':0,'이순신':0,'박자바':0}
# for x in sales.keys():
#     qty = int(input(x+' 판매수량?'))
#     sales[x] = qty
#
# print(sales)
#
# for name, qty in sales.items():
#     print(name+':', '*' * qty)

#구구단 2~9단
for y in range(2,10): #단
    print('[%d]단'%y)
    for x in range(1,10):
        print('%d * %d = %d'%(y,x,y*x))





















