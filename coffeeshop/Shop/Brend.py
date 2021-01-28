#브랜드티 메뉴 관리 모듈

from Shop.Common import *
from cx_Oracle import *

brendValue = []

class MenuB(Common):
    unit = '잔'
    count = 0
    def __init__(self):
        pass
    def __del__(self):
        MenuB.count -= 1
    @classmethod
    def printMenuQty(cls):
        print('잔수:', MenuB.count)

    def brendInput(self):
        self.brend_code = int(input('메뉴 번호는?'))
        self.brend_name = input('메뉴명은?')
        self.brend_price = int(input('가격은?'))
        print('선택이 완료 되었습니다.')

    def brendInsert(self):
        conn = connect('hr/hr@localhost:1521/xe')
        cur = conn.cursor()
        data = (self.brend_code, self.brend_name, self.brend_price)
        cur.execute('insert into brend values (:1.:2,:3,:4)', data)
        cur.close()
        conn.commit()
        conn.close()

    def brendSelect(self, data):
        conn = connect('hr/hr@localhost:1521/xe')
        cur = conn.cursor()
        cur.execute('''select * from brend where brend_name like '%' || :1 || '%' ''', data)
        for brend_code, brend_name, brend_price in cur:
            print(brend_code, brend_name, brend_price)
            brendValue.append([brend_code, brend_name, brend_price])
        cur.close()
        conn.close()

def brendMenu():
    while True:
        print('=' * 20)
        print('***브랜드 메뉴***')
        print('=' * 20)
        print('1. 메뉴를 선택')
        print('2. 메뉴를 조회')
        print('e. 이전 메뉴로')
        print('=' * 20)
        mo = input('입력 해주세요.')
        if mo == '1':
            brend = MenuB()
            brend.brendInput()
            brend.brendInsert()
        elif mo == '2':
            see = input('조회하시려면 엔터를 눌러주세요')
            brend = MenuB()
            brend.brendSelect((see,))
        elif mo == 'e':
            break
        else:
            print('번호를 다시 입력해주세요.')

def menuList():
    MenuP = Common()
    MenuP.txtRead('./Shop/brend.txt')
