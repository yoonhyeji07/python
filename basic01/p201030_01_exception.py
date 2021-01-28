#예외(exception)처리
# while True:
#     try:
#         #실행할 문장
#         a = int(input('숫자는?'))
#         print(a+100)
#         break
#     except:
#         #예외발생시 처리할 문장
#         print('숫자를 입력해 주세요!')

# a = input('숫자?')
# if a.isdigit():
#     a = int(a)
#     print(a+100)
# else:
#     print('숫자를 입력해 주세요')

#실습)나눗셈 예외처리
# def division(a,b):
#     try:
#         a = int(a) ; b=int(b)
#         result = a/b
#     except ValueError as e:
#         print('숫자를 입력해주세요')
#     except ZeroDivisionError as e:
#         print('0으로 나눌수 없습니다.')
#         print(e)
#     except Exception as e:
#         print('예외발생')
#         print(e)
#     else:  #정상수행했을때
#         print(result)
#
# #100/5 : 100=>피제수 , 5:제수
# a = input('피제수?')
# b = input('제수?')
# division(a,b)

#실습)잘못된 index접근
# try:
#     a = [1,2,3,4]
#     for x in range(5):
#         print(a[x])
# except IndexError as e:
#     print(e , '인덱스 예외')
# except Exception as e:
#     print(e)
# finally: #예외가 발생하든 안하든 무조건 실행
#     print('리스트 출력 종료')

#실습)파일 오픈 시 예외 처리

# try:
#     f = open('./data/item.txt', 'r')
# except FileNotFoundError as e:
#     print('파일이 존재하지 않습니다.')
# else: #정상수행
#     try:
#         print(f.read())
#     except UnicodeDecodeError as e:
#         print(e)
#     finally: #파일이 정상적으로 열렸을때만 close()해줄수 있다
#         f.close()

#사용자 예외발생시키기
#사용자 예외 만들기
class PositiveError(Exception):
    def __init__(self):
        super().__init__('양수를 입력해 주세요')


try:
    a = int(input('양수는?'))
    if a<=0:
        raise PositiveError
    print(a*10)
except ValueError as e:
    print('숫자를 입력해 주세요')
except PositiveError as e:
    print(e)







