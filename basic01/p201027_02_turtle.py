#거북이(그래픽모듈)
import turtle as t
p = t.Pen()
p.shape('turtle')
p.color('#ff0000')
#사각형
# for x in range(4):
#     p.forward(100)
#     p.right(360/4)
#삼각형
# for x in range(3):
#     p.forward(2)
#     p.right(360/3)
#실습)각형을 사용자에게 입력받아 그리는 함수
#함수명 : draw
#매개변수:각형
#반환형:없음
# def draw(n):
#     for x in range(n):
#         p.forward(100)
#         p.right(360/n)
# while True:
#     a = int(input('각형은?'))
#     draw(a)

# p.penup()
# p.goto(200,200)
# p.pendown()
#
# p.begin_fill()
# p.circle(100)
# p.end_fill()
#여러가지 도형 만들기
p.speed(0)#0~10 : 0이 최고속도
for x in range(200):
    p.forward(100)
    p.right(170)


t.done()


