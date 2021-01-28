import sys
#메인
from base import item
from base import company
from base import customer
# __all__ 변수 설정
# from base import *
import os
#프로그램실행시 아큐먼드 받기
import sys
# ['main.py', 'root', '1111']
# av = sys.argv
# print(av)
# if len(av) < 3:
#     print('아이디와 패스워드 입력해주세요!')
#     exit(0) #프로그램 종료
#
# if av[1]=='root' and av[2]=='1111':
#     print('슈퍼권한 유저')
# else:
#     print('일반 유저')
try:
    while True:
        #콘솔화면 지우기(콘솔에서만 동작)
        # os.system('cls')
        print('-'*15)
        print('슈퍼마켓 관리v0.1')
        print('-'*15)
        print('1.상품')
        print('2.거래처')
        print('3.고객')
        print('q.종료')
        print('-'*15)
        no = input('작업번호:')

        if no=='1': #상품
            item.itemMenu()
        elif no=='2':
            company.addCompany()
        elif no=='3':
            customer.addCustomer()
        elif no=='q':
            break
        else:
            print('잘못된 번호')
# ctrl+c
except KeyboardInterrupt :
    print('프로그램 종료!! bye~~~')
    sys.exit(0)

