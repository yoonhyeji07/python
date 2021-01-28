#파일다루기
#텍스트파일
#w:쓰기모드:기존파일삭제하고 새로운 파일생성
#a:추가모드:기존파일에 추가
# f=open('./data/sample.txt','w')
# f.write('자장면\n')
# f.write('탕수육\n')
# f.close()

#실습)사용자에게 메뉴를 입력을 받아서 파일에 저장하기
#파일명 : menu.txt
# f = open('./data/menu.txt', 'w',
#          encoding='utf-8')
# while True:
#     m = input('메뉴는?')
#     if m=='': break
#     f.write(m+'\n')
#
# f.close()

#텍스트 파일 읽기
#r:읽기모드 : 반드시 파일 존재
# f = open('./data/menu.txt', 'r',
#          encoding='utf-8')
# #전체 파일읽기
# print(f.read())
# f.close()

#한라인씩 읽기
# f=open('./data/menu.txt','r', encoding='utf-8')
# while True:
#     data=f.readline()
#     if not data: break
#     print(data,end='')
# f.close()

#여러줄 읽기
# f = open('./data/menu.txt', 'r', encoding='utf-8')
# data = f.readlines()
# print(data)
# for x in data:
#     print(x[:-1])  # 슬라이싱
# f.close()


#함수로 파일 읽어서 타입체크
# def readData():
#     f=open('./data/menu.txt','r', encoding='utf-8')
#     data = f.readlines()
#     f.close()
#     return data
#
# data = readData()
# t = type(data)
# if t==list:
#     print('리스트')

#읽기/쓰기 모드
#r+:파일이 반드시 존재
#w+:파일이 존재하지 않으면 생성
# f = open('./data/menu.txt', 'r+', encoding='utf-8')
# print(f.read())
# print('-'*10)
# f.write('짬뽕\n')
# f.seek(0) #파일의포인터위치를 처음으로 이동
# print(f.read())
# f.close()

#바이너리 파일
#
# f = open('./data/bulb.jpg', 'rb')
# w = open('./data/bulb_copy.jpg', 'wb')
# size = 1024 #1kbyte
# while True:
#     data = f.read(size)
#     if not data: break #더이상 읽어들일 파일이 없다면
#     w.write(data)
#
# f.close()
# w.close()

#실습)
# 메뉴리스트 출력
# f = open('./data/menu.txt', 'r', encoding='utf-8')
# data = f.readlines()
# print(data)
# for x in range():
# f.close()










