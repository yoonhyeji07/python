#딕셔너리
#인덱스가 없다(순서가없다)
#키와 값으로 데이터표현
# d = {'홍':90,'이':70,'유':80}
# print(d['유'])
# d['박'] = 75
# print(d)

#사용자에게 숫자를 입력받아서 해당하는 영문자 출력하기
#1:'one', 2:two ...
# dic ={1:'one',2:'two',3:'three',4:'four',5:'five'}
# no = int(input('숫자는?'))
# print(dic[no])


#학생들의 국영수 점수를 딕셔너리에 저장
#작성자 : 김성연
#버전 : 2020-10-21 v0.1
# d = {'국':100, '영':80, '수':78}
# d={}
# #입력
# kor = int(input('국어?'))
# eng = int(input('영어?'))
# math = int(input('수학?'))
# d['국'] = kor
# d['영'] = eng
# d['수'] = math
# print(d)
# #계산
# sum = d['국']+d['영']+d['수']
# avg=sum/3
# #출력
# print('합계:%d'%(sum))
# print('평균:%.2f'%(avg))

# d = {'홍':[100,90,78]}
# d={}; #s=[]
# name = input('이름은?')
# kor = int(input('국어?'))
# eng = int(input('영어?'))
# math = int(input('수학?'))
# # s.append(kor);s.append(eng);s.append(math)
# s=[kor,eng,math]
# d[name] = s
# print(d)

# d = {'홍':{'국':99,'영':80,'수':78,'총점':258,'평균':85.66}}
# s={};d={}
# name = input('이름은?')
# kor = int(input('국어?'))
# eng = int(input('영어?'))
# math = int(input('수학?'))
# summary = kor + eng + math
# avg = summary /3
# s['국']=kor; s['영']=eng; s['수']=math
# s['총점']=summary; s['평균']=float('%.2f'%avg)
# d[name] = s
# print(d)

#부울린(boolean) : True(참:1) / False(거짓:0)
# dic = {'홍':100, '박':90}
# print('홍' in dic)
# print('h' in 'hello')
# print(30 in [10,20])
# print(10 in (10,20))

#키만 알아내기
# dic = {'홍':100, '박':90}
# l = list(dic.keys()) #list형으로 변환
# print(l[0])

#값만 알아내기
# print(list(dic.values())[1])

#키와 값을 알아내기
# dic = {'홍':100, '박':90}
# print(dic.items())

#실습1)날씨 바꾸기
# dicW = {'mon':'sun', 'tue':'cloud', 'wed':'rain', 'thu':'sun', 'fri':'rain'}
# # dicW['thu'] = 'cloud'
# print(dicW)
# print(dicW.keys())
# print(dicW.values())
#
# #실습2)math 포함 여부
# dicSubject = {'kor':80,'eng':95,'math':75,'art':85}
# print('math' in dicSubject)

#실습3)학생정보 딕셔너리
# name = input('이름은?')
# age = int(input('나이는?'))
# blood = input('혈액형은?')
# dicW = {'이름': name,'나이':age,'혈액형':blood}
# print(dicW)

#실습)
# score = input('국영수점수는?').split()
# score[0] = int(score[0])
# score[1] = int(score[1])
# score[2] = int(score[2])
# print(score)
# print(tuple(map(int, score)))

# dic={'kor':score[0],}

a = {'a':100, 'b':200}
b = {'b':200, 'a':100}
print(a==b)
print(a)
print(b)



















