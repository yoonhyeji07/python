#채팅 클라이언트
import socket
from threading import Thread
HOST = '192.168.0.27' #접속할 서버의 주소
PORT = 9020

#수신받는 스레드의 함수
def rcvMsg(sock):
   while True:
      try:
         data = sock.recv(1024)
         if not data:
            break
         print(data.decode())
      except:
         pass

def runChat():
   # AF_INET : IPv4프로토콜 사용
   # SOCK_STREAM : TCP소켓
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
      sock.connect((HOST, PORT))
      t = Thread(target=rcvMsg, args=(sock,))
      t.daemon = True
      t.start()

      while True:
         msg = input()
         if msg == '/quit':
            sock.send(msg.encode())
            break

         sock.send(msg.encode())
            
runChat()
