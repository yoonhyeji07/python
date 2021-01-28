#상속
# class A:
#     a = '부모'
#     def aa(self):
#         print('부모메소드')
# class B(A):
#     b = '자식'
#     def bb(self):
#         print('자식메소드')
# class C(B):
#     c = '손주'
#     def cc(self):
#         print('손주메소드')
#
# b1 = B();print(b1.b);print(b1.a)
# b1.aa(); b1.bb()
# c1= C();print(c1.c);print(c1.a);print(c1.b)
# c1.aa(); c1.bb(); c1.cc()

#다중상속
# class ParentA:
#     pa ='부모A'
#     p = '신림동'
# class ParentB:
#     pb ='부모B'
#     p='송파동'
#
# class Child(ParentB,ParentA ):
#     c = '자식'
#
# c1 = Child()
# print(c1.pa); print(c1.pb); print(c1.c)
# print(c1.p)

# 참고:오버로딩은 파이션에서 없다
#오버라이딩 : 부모클래스의 메소드를 자식클래스가 재정의 하는것
# class Bird:
#     legs = 2
#     born = '알'
#     def fly(self):
#         print('날수있다')
#
# class Sparrow(Bird):
#     pass
#
# class Ostrich(Bird):
#     def fly(self):
#         print('날수없다')
#
# s1 = Sparrow(); print(s1.legs); print(s1.born);s1.fly()
# o1 = Ostrich(); print(o1.legs); print(o1.born);o1.fly()

#자동차 클래스
#속성 : name, color, speed, power
#기능 : powerOnOff , speedUp , speedDown
#조건 : 스피드가 0이상 300이하
class CarP: #자동차의 부모
    name = '국제자동차'
    speed = 0 #스피드 0
    power = False #파워off

    def powerOnOff(self):
        self.power = not self.power
    #현재스피드 + 1 : 100이하 이어야 한다
    def speedUp(self):
        if self.speed < 100:
            self.speed += 1
    #현재스피드 -1 : 0이상 이어야 한다
    def speedDown(self):
        if self.speed > 0:
            self.speed -= 1

class Car(CarP): #자식
    name='람보르기니'
    #public/private/protected/default
    #private속성
    __color = '검정'
    def __init__(self,color='검정'): #칼라는 default로 검정
        self.__color = color
    #오버라이딩
    #현재스피드 + 1 : 300이하 이어야 한다
    def speedUp(self):
        if self.speed < 300:
            self.speed += 1

c1 = Car('노랑') ;print(c1.power)
# print(c1.__color) 불가
c1.powerOnOff(); print(c1.power)

for x in range(310):
    c1.speedUp()
    print(c1.speed)

for x in range(310):
    c1.speedDown()
    print(c1.speed)






