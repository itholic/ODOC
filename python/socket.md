# 파이썬 소켓 사용법 (네트워크 프로그래밍)

파이썬에서 소켓을 사용해 서버-클라이언트를 구성해보자.

기본적인 개념은 일반적인 서버-클라이언트 프로그램과 동일하므로,

파이썬에서는 어떻게 구현하는지 간단한 예제를 통해 알아보자.

클라이언트에서 보내는 메시지를 서버에서 받아 그대로 출력하는 간단한 에코(echo)서버 예제이다.

## 1. 서버


```python
# echo_server.py
#-*- coding:utf-8 -*-

import socket

# 통신 정보 설정
IP = ''
PORT = 5050
SIZE = 1024
ADDR = (IP, PORT)

# 서버 소켓 설정
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind(ADDR)  # 주소 바인딩
    server_socket.listen()  # 클라이언트의 요청을 받을 준비

    # 무한루프 진입
    while True:
        client_socket, client_addr = server_socket.accept()  # 수신대기, 접속한 클라이언트 정보 (소켓, 주소) 반환
        msg = client_socket.recv(SIZE)  # 클라이언트가 보낸 메시지 반환
        print("[{}] message : {}".format(client_addr,msg))  # 클라이언트가 보낸 메시지 출력

        client_socket.sendall("welcome!".encode())  # 클라이언트에게 응답

        client_socket.close()  # 클라이언트 소켓 종료
```

통신 정보 설정에서는 IP와 POST를 묶은 주소(addr)와 수신 버퍼의 크기를 설정했다.

그 후, 주소를 바인딩하고 클라이언트의 요청을 받을 준비를 한다.

무한루프에 들어가 accept() 상태로 대기한다. 

클라이언트가 보낸 메시지를 출력하고, 

클라이언트에게 "welcome!" 이라는 메시지를 반환하는 간단한 프로그램이다


- 주요메서드: bind, listen, accept, recv, send

## 2. 클라이언트

```python
# echo_client.py
#-*- coding:utf-8 -*-

import socket

# 접속 정보 설정
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5050
SIZE = 1024
SERVER_ADDR = (SERVER_IP, SERVER_PORT)

# 클라이언트 소켓 설정
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(SERVER_ADDR)  # 서버에 접속
    client_socket.send('hi'.encode())  # 서버에 메시지 전송
    msg = client_socket.recv(SIZE)  # 서버로부터 응답받은 메시지 반환
    print("resp from server : {}".format(msg))  # 서버로부터 응답받은 메시지 출력
```

클라이언트는 더 간단하다.

서버에 접속할 정보를 설정하고,

설정한 정보를 통해 접속 후 메시지를 전송한다.

그리고 서버로부터 응답받은 메시지(welcome!)를 받아 출력 하고, 종료한다.

- 주요 메서드: connect, send, recv
