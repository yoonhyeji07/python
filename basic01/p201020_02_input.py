#사용자입력받기
#input()함수
# a=input('이름을 입력 :')
# print('당신의 이름은 %s입니다'%a)

#형변환함수(int(), float(), str())
# a=int(input('숫자는?'))
# print(a+100)

#반지름(실수)을 입력받고 원의 넓이 구하기
#원의 넓이 : r * r * 3.14
# r = float(input('반지름?'))
# print('반지름:', r*r*3.14)

#입력받은 수로 사칙연산
# a = float(input('첫번째수:'))
# b = float(input('두번째수:'))
# print('%.2f + %.2f = %.2f'%(a,b,a+b))
# print('%.2f - %.2f = %.2f'%(a,b,a-b))
# print('%.2f * %.2f = %.2f'%(a,b,a*b))
# print('%.2f / %.2f = %.2f'%(a,b,a/b))

#식까지 입력
#eval:보안취약
# cal = input('계산식은?')
# print(eval(cal))

# import os
# os.system('chcp 65001')
# cal = input('계산식은?')
# print(eval(cal))
# print(eval("__import__('os').system('dir')"))








