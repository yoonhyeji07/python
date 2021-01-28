#클라이언트
import socket
server_addr = 'B8:27:EB:33:8D:B9' #서버측 MAC주소(rasp77)
port=3 #임의의 포트번호 서버와 일치
size=1024
s=socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((server_addr,port))
try:
    while True:
        sendMsg = input('sendMsg:')
        if sendMsg =='quit':
            break
        s.send(sendMsg.encode())
        recvMsg = s.recv(size)#서버의 응답메시지
        print(recvMsg.decode())
except:
    print('예외발생')
finally:
    s.close() #소켓 닫기