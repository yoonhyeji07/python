dic={'영업시간':'AM9:00~PM:06:00','주소':'신림역7번출구'}
while True:
    msg = input('질문?')
    msg = msg.upper() #대문자로 바꾸기
    if msg=='QUIT':
        print('질의응답을 종료합니다.')
        break
    for x in dic.keys():
        if msg in x:
            sendMsg = dic[x]
            break
    else:
        sendMsg='담당자에게 문의해 주세요'
    print(sendMsg)