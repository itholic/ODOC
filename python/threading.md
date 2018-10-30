# threading

파이썬에서는 threading 모듈을 통해 손쉽게 쓰레드를 구현할 수 있다.

아래는 worker라는 메소드를 쓰레드를 통해 동시에 10개 실행시키는 예제이다.

worker는 실행 후 5초 후에 종료된다.

```python
#-*- coding:utf-8 -*-

import threading
import time


def worker(msg):
    """ start 하면서 전달받은 msg 출력, 5초 후에 종료 """
    # 쓰레드 생성시 지정해준 name과 인자로 받은 msg 출력
    print("{} is start : {}".format(threading.currentThread().getName(), msg))
    time.sleep(5)
    print("{} is end".format(threading.currentThread().getName()))


def main():
    for i in range(10):
        # 쓰레드는 threading.Thread 메소드를 써서 만들면 된다
        # target에는 쓰레드로 띄울 함수명을 넣어주면 된다
        # name으로 쓰레드의 이름을 지정할 수 있다.
        # args로 함수의 인자를 넘겨줄 수 있다.
        # 이름은 threading.currentThread().getName()로 확인 가능하다.
        msg = "hello {}".format(i)
        th = threading.Thread(target=worker, name="[th def {}]".format(i), args=(msg,))
        th.start()  # 위에서 생성한 쓰레드를 시작한다


if __name__ == "__main__":
    main()
```

실행시키면 다음과 같은 결과가 나온다


```python
[th def 0] is start : hello 0
[th def 1] is start : hello 1
[th def 2] is start : hello 2
[th def 3] is start : hello 3
[th def 4] is start : hello 4
[th def 5] is start : hello 5
[th def 6] is start : hello 6
[th def 7] is start : hello 7
[th def 8] is start : hello 8
[th def 9] is start : hello 9
[th def 0] is end
[th def 1] is end
[th def 3] is end
[th def 4] is end
[th def 2] is end
[th def 5] is end
[th def 7] is end
[th def 6] is end
[th def 8] is end
[th def 9] is end
```

시작은 0번부터 9번까지 순차적으로 됐지만,

동시에 실행되므로 종료시점은 뒤섞여있는것을 확인할 수 있다.

쓰레드는 다음과 같이 클래스도로 사용 가능하다.

```
#-*- coding:utf-8 -*-

import threading
import time

class Worker(threading.Thread):
    """클래스 생성시 threading.Thread를 상속받아 만들면 된다"""

    def __init__(self, args, name=""):
        """__init__ 메소드 안에서 threading.Thread를 init한다"""
        threading.Thread.__init__(self)
        self.name = name
        self.args = args

    def run(self):
        """start()시 실제로 실행되는 부분이다"""
        print("{} is start : {}".format(threading.currentThread().getName(), self.args[0]))
        time.sleep(5)
        print("{} is end".format(threading.currentThread().getName()))


def main():
    for i in range(10):
        # threading.Thread 대신, 클래스명으로 쓰레드 객체를 생성하면 된다
        msg = "hello"
        th = Worker(name="th cls {}".format(i), args=(msg,))
        th.start()  # run()에 구현한 부분이 실행된다

if __name__ == "__main__":
    main()

```

결과는 아래와 같다.

메소드로 만들었을때와 똑같다.

```python
th cls 0 is start : hello
th cls 1 is start : hello
th cls 2 is start : hello
th cls 3 is start : hello
th cls 4 is start : hello
th cls 5 is start : hello
th cls 6 is start : hello
th cls 7 is start : hello
th cls 8 is start : hello
th cls 9 is start : hello
th cls 0 is end
th cls 1 is end
th cls 2 is end
th cls 3 is end
th cls 6 is end
th cls 4 is end
th cls 5 is end
th cls 7 is end
th cls 9 is end
th cls 8 is end
```

### 데몬(Daemon) 쓰레드

쓰레드를 데몬으로 만들어서 사용할 수도 있다.

주요 작업을 하는 메인 쓰레드가 따로 있고, 백그라운드 작업을 위한 쓰레드를 띄울 수 있다는 것이다.

이러한 백그라운드 작업을 데몬으로 띄우지 않으면, 백그라운드 작업을 하는 쓰레드가 종료될때까지 메인 프로그램도 종료되지 않는다.

프로그램의 상태를 모니터링 하는 프로그램이 내부에서 주기적으로 동작하는데, 

만약 이 프로그램 때문에 메인 프로그램이 종료되지 못하면 이상하다.

데몬쓰레드는 메인 프로그램이 종료될때 자동으로 같이 종료된다.

즉, 정기적이고 부수적인 작업은 데몬으로, 필수적인 메인 작업은 일반 쓰레드로 띄운다.

예제를 보자.

```python
#-*- coding:utf-8 -*-

import threading
import time


def worker(msg):
    print("{} is start : {}".format(threading.currentThread().getName(), msg))
    time.sleep(5)
    print("{} is end".format(threading.currentThread().getName()))


def main():
    msg = "hello"
    th = threading.Thread(target=worker, name="[Daemon]", args=(msg,))
    th.setDaemon(True)
    th.start()

    print("Main Thread End")

if __name__ == "__main__":
    main()
```

위와 똑같은 예제에서, th.setDamon(True) 만 추가되었다.

그리고 쓰레드를 10개가 아닌 1개만 실행시켰다.

그럼 결과를 보자.

```html
[Daemon] is start : hello
Main Thread End
```

쓰레드가 시작만되고 종료되지 않았다.

이는 메인 프로그램이 종료되면서 데몬 쓰레들이 자동으로 같이 종료되었기 떄문이다.

하지만 다음과 같이 join 메소드를 써서 메인 프로그램이 데몬 쓰레드가 종료될 때까지 기다리도록 할 수도 있다.

```python
#-*- coding:utf-8 -*-

import threading
import time


def worker(msg):
    print("{} is start : {}".format(threading.currentThread().getName(), msg))
    time.sleep(5)
    print("{} is end".format(threading.currentThread().getName()))


def main():
    msg = "hello"
    th = threading.Thread(target=worker, name="[Daemon]", args=(msg,))
    th.setDaemon(True)
    th.start()
    th.join()

    print("Main Thread End")

if __name__ == "__main__":
    main()
```

결과를 보자

```
[Daemon] is start : hello
[Daemon] is end
Main Thread End
```

join 부분에서 데몬 쓰레드가 종료될 때까지 기다렸다가 메인 쓰레드가 수행된 것을 확인할 수 있다.