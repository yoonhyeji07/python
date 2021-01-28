#커피 메뉴 관리 모듈

from Shop.Common import *
from cx_Oracle import *

coffeeValue = []

class MenuC(Common):
    unit = '잔'
    count = 0
    def __init__(self):
        pass
    def __del__(self):
        MenuC.count -= 1

    @classmethod
    def printMenuQty(cls):
        print('잔수:',MenuC.count)

    def coffeeInput(self):
        self.coffee_code = int(input('메뉴 번호는?'))
        self.coffee_name = input('메뉴명은?')
        self.coffee_price = int(input('가격은?'))
        print('선택이 완료 되었습니다.')
    
    def coffeeInsert(self):
        conn = connect('hr/hr@localhost:1521/xe')
        cur = conn.cursor()
        data = (self.coffee_code,self.coffee_name,self.coffee_price)
        cur.execute('insert into coffee values (:1.:2,:3,:4)',data)
        cur.close()
        conn.commit()
        conn.close()

    def coffeeSelect(self,data):
        conn = connect('hr/hr@localhost:1521/xe')
        cur = conn.cursor()
        cur.execute('''select * from coffee where coffee_name like '%' || :1 || '%' ''',data)
        for coffee_code, coffee_name, coffee_price in cur:
            print(coffee_code,coffee_name,coffee_price)
            coffeeValue.append([coffee_code,coffee_name,coffee_price])
        cur.close()
        conn.close()

def coffeeMenu():
    while True:
        print('='*20)
        print('***커피 메뉴***')
        print('='*20)
        print('1. 메뉴를 선택')
        print('2. 메뉴를 조회')
        print('e. 이전 메뉴로')
        print('='*20)
        mo = input('입력 해주세요.')
        if mo == '1':
            coffee = MenuC()
            coffee.coffeeInput()
            coffee.coffeeInsert()
        elif mo == '2':
            see = input('조회 하시려면 엔터를 눌러주세요.')
            coffee = MenuC()
            coffee.coffeeSelect((see,))
        elif mo == 'e': break
        else:
            print('번호를 다시 입력해주세요.')

# def coffeeInout():
#     print('메뉴를 장바구니에 담았습니다.')
    # code = input('취소할 메뉴 번호는?')
    # name = input('취소할 메뉴명은?')
    # coffee = MenuC(code,name)
    # coffee.txtRead('./Shop/coffee.txt', data)

def menuList():
    MenuP = Common()
    MenuP.txtRead('./Shop/coffee.txt')
