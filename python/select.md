# I/O 멀티플렉싱

select모듈을 다루기 전에 I/O 멀티플렉싱이 무엇인지 간단하게 알아보고 넘어가자.

우선 간단하게 한 줄로 정리를 하자면,

"한 개의 프로세스로 두 개 이상의 클라이언트 요청을 처리하는 것" 이다.

이제 예제로 알아보자.

저번에 정리했던 <a href="https://itholic.github.io/python-socket/" target="_blank">파이썬 소켓 사용법</a>의 서버 코드를 가져와보자.

```python
  1 #-*- coding:utf-8 -*-
  2
  3 import socket
  4
  5 # 접속 정보 설정
  6 IP = ''
  7 PORT = 5050
  8 SIZE = 1024
  9 ADDR = (IP, PORT)
 10
 11 # 서버 소켓 설정
 12 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
 13     server_socket.bind(ADDR)  # 주소 바인딩
 14     server_socket.listen()  # 클라이언트의 요청을 받을 준비
 15
 16     # 무한루프 진입
 17     while True:
 18         client_socket, client_addr = server_socket.accept()  # 수신대기, 접속한 클라이언트 정보 (소켓, 주소) 반환
 19         print('hi')
 20         msg = client_socket.recv(SIZE)  # 클라이언트가 보낸 메시지 반환
 21         print("[{}] message : {}".format(client_addr,msg))  # 클라이언트가 보낸 메시지 출력
 22
 23         client_socket.sendall("welcome!".encode())  # 클라이언트에게 응답
 24
 25         client_socket.close()  # 클라이언트 소켓 종료
```

18번째 줄에서 accept() 메소드를 통해 클라이언트의 접속을 대기하고있다.

그리고 클라이언트가 접속하면 클라이언트 소켓을 가지고 다음 동작을 수행하고있다.

현재 5050 포트를 처리하는 소켓 하나만 정의했으므로, 이런 방식으로 처리해도 큰 무리가 없다.


<br/>

하지만 실제로는 한 번에 여러 포트로 접속하는 클라이언트를 동시에 처리해야하는 경우가 많다.

해당 예제에서는 5050포트만 열어놓고 있지만,

5050, 5060 두 개의 포트를 동시에 열어놓고,

각 포트로 들어오는 클라이언트마다 다른 처리를 하고 싶다.

위 코드를 다음과 같이 변경해보자.

```python
  5 # 접속 정보 설정
  6 IP = ''
  7 PORT1 = 5050
  8 PORT2 = 5060
  9 SIZE = 1024
 10 ADDR1 = (IP, PORT1)
 11 ADDR2 = (IP, PORT2)
 12
 13 # 서버 소켓1 설정
 14 server_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 15 server_socket1.settimeout(1)
 16 server_socket1.bind(ADDR1)  # 주소 바인딩
 17 server_socket1.listen()  # 클라이언트의 요청을 받을 준비
 18
 19 # 서버 소켓2 설정
 20 server_socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 21 server_socket2.settimeout(1)
 22 server_socket2.bind(ADDR2)  # 주소 바인딩
 23 server_socket2.listen()  # 클라이언트의 요청을 받을 준비
 24
 25 # 무한루프 진입
 26 while True:
 27     try:
 28         print('hello socket1')
 29         client_socket, client_addr = server_socket1.accept()  # 수신대기, 접속한 클라이언트 정보 (소켓, 주소) 반환
 30         msg = client_socket.recv(SIZE)  # 클라이언트가 보낸 메시지 반환
 31         print("[{}] message : {}".format(client_addr,msg))  # 클라이언트가 보낸 메시지 출력
 32
 33         client_socket.sendall("welcome 5050!".encode())  # 클라이언트에게 응답
 34
 35         client_socket.close()  # 클라이언트 소켓 종료
 36     except KeyboardInterrupt:
 37         raise KeyboardInterrupt
 38     except:
 39         pass
 40
 41     try:
 42         print('hello socket2')
 43         client_socket, client_addr = server_socket2.accept()  # 수신대기, 접속한 클라이언트 정보 (소켓, 주소) 반환
 44         msg = client_socket.recv(SIZE)  # 클라이언트가 보낸 메시지 반환
 45         print("[{}] message : {}".format(client_addr,msg))  # 클라이언트가 보낸 메시지 출력
 46
 47         client_socket.sendall("welcome 5060!".encode())  # 클라이언트에게 응답
 48
 49         client_socket.close()  # 클라이언트 소켓 종료
 50     except KeyboardInterrupt:
 51         raise KeyboardInterrupt
 52     except:
 53         pass
```

기존의 코드와 직관적인 비교를 위해, 

그리고 설명의 용이함을 위해 추상화 하지 않고 코드를 모두 입력했다.

바뀐 부분을 위주로 차근차근 훑어보자.

<br/>

우선 8번째 줄에 5060이라는 포트를 하나 추가했다.

포트를 추가했으므로 해당 포트로 들어오는 클라이언트를 처리하기 위해 소켓도 추가해야한다.

그래서 20~23번쨰 줄에 소켓을 하나 더 추가했다.

<br/>

15, 21번째 줄을 보면 settimeout(1) 이라는 녀석도 추가됐다.

이 부분이 block 소켓을 non_block으로 처리 가능하게 해주는 핵심적인 부분이다.

이는 accept()를 통해 클라이언트의 접속을 1초간 기다리다가,

1초가 지나도 접속이 없으면 socket.timeout 예외를 발생시킨다는 의미이다.

그래서 38, 52번째 줄에 socket.timeout 발생시 다음 코드로 그냥 pass하도록 예외처리했다.

<br/>

이제 서버를 실행해보면, 

다음과 같이 1초 간격으로 번갈아가며 'hello socket1', 'hello socket2'가 출력되는 것을 확인할 수 있다.

```
# python echo_server.py
hello socket1
hello socket2
hello socket1
hello socket2
hello socket1
hello socket2
hello socket1
hello socket2
```

'hello socket1'이 떠있을 때에는 5050포트로 접속하는 클라이언트를,

'hello socket2'가 떠있을 때에는 5060포트로 접속하는 클라이언트를 처리할것이다.

echo_client_5050.py는 5050포트로 접속하는 클라이언트,

echo_client_5060.py는 5060포트로 접속하는 클라이언트이다.

```
# python echo_server.py
hello socket1
hello socket2
hello socket1
[('127.0.0.1', 59744)] message : b'hi'     << echo_client_5050.py 실행 시점
hello socket2
hello socket1
hello socket2
hello socket1
hello socket2
[('127.0.0.1', 59745)] message : b'hi'     << echo_client_5060.py 실행 시점
hello socket1
hello socket2

# python echo_client_5050.py
resp from server : b'welcome 5050!'

# python echo_client_5060.py
resp from server : b'welcome 5060!'
```

참고로 echo_client 코드는 다음과 같다.

뒤에 붙은 숫자에 따라 SERVER_PORT 값만 다르다.

```python
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

어쨌든 이렇게 처리하는 방식을 I/O 멀티플렉싱이라고 한다.

한 개의 프로세스가 두 군데 이상의 클라이언트로부터의 요청을 처리하는 것이다.

# select

이제 드디어 select에 대한 이야기를 해보자.

앞선 예제에서 어쨌든 두 개 이상의 포트를 처리 하긴 했는데 뭔가 찝찝하다.

클라이언트의 접속이 없음에도 불구하고 서버가 계속 소켓을 차례로 돌며 accept 호출을 반복하고있다.

그 증거로 서버만 실행시켜 놓았는데도 'hello socket1', 'hello socket2'가 무한히 출력되고있다.

<br/>

위 예제에서는 2개의 포트만 열어두었기 때문에 서로 1초씩만 번갈아 대기하면 되지만,

만약 10개의 포트를 열어두는 경우에는 10초가 지나야 한 소켓의 순서가 돌아오게 된다.

어떤 클라이언트는 재수없으면 서버에 접속을 요청하고 10초 후에나 접속이 된다는 것이다.

서버가 처리하고있는 다른 클라이언트가 전혀 없음에도 불구하고 말이다.

<br/>

이처럼 timeout 설정을 통해 다중 포트를 처리하긴 했지만, 여전히 비효율적인 부분이 존재한다.

바로 이러한 상황에서 더욱 효율적인 I/O 멀티플렉싱을 구현하기 위해 select라는 모듈을 사용한다.

다음 코드를 보자.


```
  1 #-*- coding:utf-8 -*-
  2
  3 import socket
  4 import select
  5
  6 # 접속 정보 설정
  7 IP = ''
  8 PORT1 = 5050
  9 PORT2 = 5060
 10 SIZE = 1024
 11 ADDR1 = (IP, PORT1)
 12 ADDR2 = (IP, PORT2)
 13
 14 # 서버 소켓1 설정
 15 server_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 16 server_socket1.bind(ADDR1)  # 주소 바인딩
 17 server_socket1.listen()  # 클라이언트의 요청을 받을 준비
 18
 19 # 서버 소켓2 설정
 20 server_socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 21 server_socket2.bind(ADDR2)  # 주소 바인딩
 22 server_socket2.listen()  # 클라이언트의 요청을 받을 준비
 23
 24 # read 소켓 리스트
 25 read_socket_list = [server_socket1, server_socket2]
 26
 27 # 무한루프 진입
 28 while True:
 29     # select 선언
 30     conn_read_socket_list, conn_write_socket_list, conn_except_socket_list = select.select(read_socket_list, [], [])
 31     for conn_read_socket in conn_read_socket_list:
 32         if conn_read_socket == server_socket1:
 33             print('hello socket1')
 34             client_socket, client_addr = server_socket1.accept()  # 수신대기, 접속한 클라이언트 정보 (소켓, 주소) 반환
 35             msg = client_socket.recv(SIZE)  # 클라이언트가 보낸 메시지 반환
 36             print("[{}] message : {}".format(client_addr,msg))  # 클라이언트가 보낸 메시지 출력
 37
 38             client_socket.sendall("welcome 5050!".encode())  # 클라이언트에게 응답
 39
 40             client_socket.close()  # 클라이언트 소켓 종료
 41         elif server_socket2 == server_socket2:
 42             print('hello socket2')
 43             client_socket, client_addr = server_socket2.accept()  # 수신대기, 접속한 클라이언트 정보 (소켓, 주소) 반환
 44             msg = client_socket.recv(SIZE)  # 클라이언트가 보낸 메시지 반환
 45             print("[{}] message : {}".format(client_addr,msg))  # 클라이언트가 보낸 메시지 출력
 46
 47             client_socket.sendall("welcome 5060!".encode())  # 클라이언트에게 응답
 48
 49             client_socket.close()  # 클라이언트 소켓 종료

```

전체적인 모양은 비슷한데, 뭔가 중간중간 바뀌었다.

우선 더이상 settimeout() 메소드를 통해 timeout을 설정하지 않아도 된다.

대신 25번째 줄에서 접속을 대기할 소켓 리스트를 만들어주고,

30번째 줄에서 select.select() 메소드의 첫 번쨰 인자로 해당 리스트를 넘겨주었다.

<br/>

이제 앞선 예제처럼 server_socket1과 server_socket2를 번갈아가며 accept() 하지 않는다.

대신 select.select()를 수행한 라인에서 read_socket_list에 포함된 소켓 중 하나가 접속할 때까지 대기한다.

실제로 다음과 같이 서버를 실행했을 때, 클라이언트가 접속할 때까지 아무런 일도 일어나지 않는다.

```
# python echo_server.py
(클라이언트 대기중)
```

그리고 클라이언트가 접속할 때에만 다음과 같이 각 클라이언트에 적합한 작업을 수행한다.

```
# python echo_server.py
hello socket1
[('127.0.0.1', 60229)] message : b'hi'     << echo_client_5050 수행 시점
hello socket2
[('127.0.0.1', 60230)] message : b'hi'     << echo_client_5060 수행 시점

# python echo_client_5050.py
resp from server : b'welcome 5050!'

# python echo_client_5060.py
resp from server : b'welcome 5060!'
```

프로세스가 block이 되어있긴 하지만, 

여러 포트로의 접속을 동시에 받아들일 준비가 되어있는 상태인 것이다.

32, 41번째 줄에서 각각의 포트로 들어온 클라이언트에 대한 처리 방식을 기술하고있다.

<br/>

앞선 예제와의 차이가 잘 느껴지지 않는다면 이렇게 생각하자.

음식점에서 예약손님 두 테이블을 받기위해 방 2개를 준비해놓았다.

기존 방식의 경우 손님이 언제 올지 모르기에 방 두개를 계속 왔다갔다하며 손님이 왔는지 체크하고있다.

1초에 한 번씩 방을 번갈아가며 왔다갔다 하다가, 손님이 왔을 때 일을 시작한다.

<br/>

select를 사용한 예제의 경우에는 조금 다르다.

마찬가지로 예약손님 두 테이블을 받기 위해 방 2개를 준비해 놓았지만,

두 방을 동시에 모니터링 할 수 있는 CCTV를 설치한 것이다.

그래서 손님이 올 때까지만 CCTV를 보며 가만히 대기하다가, 손님이 왔을때 나가서 일을 시작한다.

<br/>

모든 프로그래밍이 다 똑같지만,

네트워크 프로그래밍, 특히 select 부분은 직접 실행해보지 않으면 감을 잡기가 매우 어렵다.

하지만 어렵게 익힌 기술일수록 적용했을때 어마어마한 힘을 발휘하는 법이다.

앞으로는 select를 사용하여 고급지게(?) I/O 멀티플렉싱을 구현해보자.
