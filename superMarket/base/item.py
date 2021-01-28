from base.common import *
from cx_Oracle import *

globalValue =[]
#상품관리모듈
class ItemP(Common):
    unit='개'
    count=0 #상품의 갯수
    def __init__(self):
        pass
    def __del__(self):
        ItemP.count -= 1  # 상품의 갯수 - 1

    #상품의 수량을 출력하는 메소드
    #어노테이션:클래스 메소드
    #클래스필드를 출력하기 위해서
    @classmethod
    def printItemQty(cls):
        print('수량:', ItemP.count)

    #상품입력받기
    def itemInput(self):
        self.code = input('상품코드는?')
        self.itemname = input('상품명은?')
        self.price = int(input('가격은?'))
        self.bigo = input('비고?')

    #db insert
    def itemInsert(self):
        conn = connect('hr/hr@localhost:1521/xe')
        cur= conn.cursor()
        data = (self.code,self.itemname, self.price, self.bigo)
        cur.execute('insert into item values (:1,:2,:3,:4)', data)
        cur.close()
        conn.commit()
        conn.close()

    #db select
    def itemSelect(self,data):
        conn = connect('hr/hr@localhost:1521/xe')
        cur= conn.cursor()
        cur.execute(''' select * from item  
            where itemname like '%' || :1 || '%' ''', data)
        for code, itemname, price, bigo in cur:
            print(code, itemname, price, bigo)
        globalValue.append([code,itemname, price, bigo])
        cur.close()
        conn.close()

# 서브메뉴
def itemMenu():
    while True:
        print('*'*15)
        print('*상품관리*')
        print('*'*15)
        print('1.상품등록')
        print('2.상품조회')
        print('q.메인메뉴')
        print('*'*15)
        no = input('작업번호:')
        if no=='1': #등록
            item = ItemP()#객체생성
            item.itemInput() #입력받기
            item.itemInsert() #추가하기
        elif no == '2': #조회
            find = input('조회할 상품명은?')
            item = ItemP()  # 객체생성
            item.itemSelect((find,)) #조회하기
            input('조회 완료....')
        elif no=='q':
            break
        else:
            print('잘못된 번호')



