from Shop import ade
from Shop import Brend
from Shop import Coffee
from cx_Oracle import *

while True:
    print('='*20)
    print('1. 매장에서 먹고 갈래요')
    print('2. 포장해서 갈래요')
    print('='*20)
    view = input('방법을 선택해주세요')
    if view == '1':
            print('매장으로 진행됩니다.')
            break
    elif view == '2':
            print('포장으로 진행됩니다.')
            break
    else:
            print('다시 선택해주세요 ')

while True:
    print('='*20)
    print('***커피숍 메뉴***')
    print('='*20)
    print('1.에이드 종류')
    print('2.브랜드 종류')
    print('3.커피 종류')
    print('e.시스템 종료')
    print('='*20)
    mo = input('메뉴를 선택해주세요.')

    if mo == '1':
        from Shop import ade
        ade.adeMenu()
    elif mo == '2':
        from Shop import Brend
        Brend.brendMenu()
        MenuB()
    elif mo == '3':
        from Shop import Coffee
        Coffee.coffeeMenu()
        MenuC()
    elif mo == 'e': break
    else:
        print('번호를 다시 입력해주세요.')

input('엔터를 입력하시면 종료됩니다.')

