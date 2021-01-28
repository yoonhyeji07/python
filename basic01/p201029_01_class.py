#클래스:객체를 만들기 위한 틀
# class Dog:
#     #속성:필드
#     type = '강아지'
#     color = '검정색'
#     eyes = 2
#     legs = 4
#     #기능:메소드
#     def walk(self):
#         print('걸어갑니다.')
#     def eat(self):
#         print('먹는다')
#     def run(self):
#         print('뛴다')
#
# d1=Dog();print(d1.type); d1.eat()
# d2=Dog();print(d2.type); d2.eat()

#실습)계산기 객체
# class Cal:
#     color = '흰색' #필드
#     def add(self,a,b):
#         return a+b #지역변수
#     def sub(self,a,b):
#         return a-b
#     def mul(self,a,b):
#         return a*b
#     def div(self,a,b):
#         return a/b
#
# c1 = Cal()
# print(c1.color)
# print('더하기:',c1.add(20,10))
# print('빼기:',c1.sub(20,10))
# print('곱하기:',c1.mul(20,10))
# print('나누기:',c1.div(20,10))

#클래스 필드/ 인스턴스 필드
# class Cat:
#     #클래스 필드 : 공통필드
#     jong = '고양이'
#     sound='야옹'
#     #self : 객체자기 자신 : 객체의 필드
#     def eat(self,name):
#         self.name = name #인스턴스 필드
#         print(self.name , '먹는다')
#
# c1=Cat(); c1.eat('나비') ; print(c1.name)
# c2=Cat(); c2.eat('야옹이'); print(c2.name)
# Cat.sound='이야용'; c1.sound = '냐옹'
# print(c1.sound); print(c2.sound)

#클래스의 생성자
# class Cat:
#     #생성자:객체가 생성될때 자동으로 실행되는 메소드
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color
#
#     def walk(self):
#         print(self.name , '걷는다')
#
# c1 = Cat('나비','흰색')
# c1.walk(); print(c1.name)
# c2 = Cat('야용','검정')
# c2.walk(); print(c2.name)

# #상품(공산품)클래스
# class ItemP:
#     type ='공산품'
#     unit='개'
#     count=0 #상품의 갯수
#     def __init__(self,code, name, price):
#         self.code = code
#         self.name = name
#         self.price = price
#         ItemP.count += 1 #상품의 갯수 + 1
#         # print(self.name, '생성')
#         # self.printItem()
#
#     def __del__(self):
#         ItemP.count -= 1  # 상품의 갯수 - 1
#         # print(self.name, '삭제')
#     #상품의 수량을 출력하는 메소드
#     #어노테이션:클래스 메소드
#     @classmethod
#     def printItemQty(cls):
#         print('수량:', ItemP.count)
#
# itemList =[]
# while True:
#     code = input('코드는?')
#     if code == 'q': break
#     name =input('이름은?')
#     price = int(input('가격은?'))
#     item = ItemP(code,name,price)
#     itemList.append(item)
#     print('*' * 15)
#
# ItemP.printItemQty()
#엔터가 입력되면 프로그램이 종료되면서 메모리 객체 자동삭제
# input('엔터')

#실습)영화티켓
#1)
# class Ticket:
#     count ={'터미네이터':20,'매트릭스':20}
#     def __init__(self,name): #생성자
#         self.name = name
#         self.count[name] -= 1
#         print(self.name, '1장 판매')
#         self.printTicketCount()
#     def __del__(self): #소멸자
#         self.count[self.name] += 1
#
#     def printTicketCount(self):
#         print(self.name, '잔여:',self.count[self.name])
#
# t1 = Ticket('터미네이터')
# t2 = Ticket('터미네이터')
# t3 = Ticket('매트릭스')

class Ticket:
    count ={'터미네이터':[20,8000],'매트릭스':[20,9000]}
    def __init__(self,name,qty):
        self.name = name
        self.count[name][0] -= qty
        self.qty = qty
        print(self.name, qty, '장 판매')

    def printTicketCount(self):
        print(self.name, '구매가격:',self.count[self.name][1] * self.qty)
        print(self.name, '잔여:',self.count[self.name][0])

    def __del__(self): #소멸자
        self.count[self.name] += self.qty

name = input('영화제목은?')
qty = int(input('장수?'))
t1 = Ticket('터미네이터',qty)

name = input('영화제목은?')
qty = int(input('장수?'))
t2 = Ticket('매트릭스',qty)
print('판매리스트')
t1.printTicketCount()
t2.printTicketCount()







