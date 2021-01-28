#서버
#소켓:창구 ..소켓을 열어야 통신 가능
#소켓을 열려면 mac(ip), 포트번호, 프로토콜 
#osi모델 중 전송계층
import socket
server_addr='B8:27:EB:33:8D:B9' #서버측 MAC주소(rasp77)
port=3 #임의의 포트번호 클라이언트와 일치
backlog=1 #클라이언트의 대기허용 갯수
size=1024
s=socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((server_addr,port))
s.listen(backlog)
client, client_address = s.accept()

try:
    while True:
        recvMsg = client.recv(size)
        if recvMsg:
            recvMsg = recvMsg.decode() #받은 메시지 디코딩
            print(recvMsg)
            sendMsg = "ok:"+recvMsg
            client.send(sendMsg.encode()) #보낼 메시지 인코딩 
except:
    client.close() #클라이언트 접속 해제
    s.close()     #소켓 접속 해제

