#에이드 메뉴

from Shop.Common import *
from cx_Oracle import *

adeValue = []

class MenuA(Common):
    unit = '잔'
    count = 0
    def __init__(self):
        pass
    def __del__(self):
        MenuA.count -= 1
    @classmethod
    def printMenuQty(cls):
        print('잔수:', MenuA.count)

    def adeInput(self):
        self.ade_code = int(input('메뉴 번호는?'))
        self.ade_name = input('메뉴명은?')
        self.ade_price = int(input('가격은?'))
        print('선택이 완료 되었습니다.')

    def adeInsert(self):
        conn = connect('hr/hr@localhost:1521/xe')
        cur = conn.cursor()
        data = (self.ade_code, self.ade_name, self.ade_price)
        cur.execute('insert into ade values (:1.:2,:3,:4)', data)
        cur.close()
        conn.commit()
        conn.close()

    def adeSelect(self, data):
        conn = connect('hr/hr@localhost:1521/xe')
        cur = conn.cursor()
        cur.execute('''select * from ade where ade_name like '%' || :1 || '%' ''', data)
        for ade_code, ade_name, ade_price in cur:
            print(ade_code, ade_name, ade_price)
            adeValue.append([ade_code, ade_name, ade_price])
        cur.close()
        conn.close()

def adeMenu():
    while True:
        print('=' * 20)
        print('***에이드 메뉴***')
        print('=' * 20)
        print('1. 메뉴를 선택')
        print('2. 메뉴를 조회')
        print('e. 이전 메뉴로')
        print('=' * 20)
        mo = input('입력 해주세요')
        if mo == '1':
            ade = MenuA()
            ade.adeInput()
            ade.adeInsert()
        elif mo == '2':
            see = input('조회하시려면 엔터를 눌러주세요')
            ade = MenuA()
            ade.adeSelect((see,))
        elif mo == 'e':
            break
        else:
            print('번호를 다시 입력해주세요.')

def menuList():
    #ade.txt파일 만들고 파일 조회

    MenuP = Common()

    MenuP.txtRead('./Shop/ade.txt')
