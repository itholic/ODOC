# queue

파이썬에서는 Queue자료구조를 손쉽게 활용할 수 있는 모듈을 제공한다.

다음과 같이 Queue를 선언하고 데이터를 넣으면, 집어넣은 순서대로(FIFO) 데이터를 가져온다.

* FIFO : First In, First Out (선입선출)

```python
#-*- coding:utf-8 -*-

import Queue

q = Queue.Queue()  # 큐 선언

# 데이터 리스트 선언 및 데이터 삽입
data_list = []

data_list.append('one')
data_list.append('two')
data_list.append('three')
data_list.append('four')
data_list.append('five')
data_list.append('six')
data_list.append('seven')
data_list.append('eight')
data_list.append('nine')
data_list.append('ten')

# 큐에 데이터 삽입
for data in data_list:
    q.put(data)

# 큐에 넣은 데이터 확인
while q.qsize():
    print(q.get())  # one, two ~ nine, ten 순서대로 출력
```

그런데 만약, 

1. put을 할때 큐가 꽉차있거나 (queue overflow)

2. get을 할 때 큐가 비어있다면 (queue underflow)

해당 프로세스는 큐에서 데이터가 빠지거나 들어올때까지 영원히 대기하게 된다.(데드락)

이는 put과 get함수가 기본적으로 blocking 함수이기 때문인데,

이를 방지하기 위해서는 다음과 같이 put_nowait 함수와 get_nowait 함수를 사용하면 된다.


```python
#-*- coding:utf-8 -*-

import Queue

q = Queue.Queue()  # 큐 선언

# 데이터 리스트 선언 및 데이터 삽입
data_list = []

data_list.append('one')
data_list.append('two')
data_list.append('three')
data_list.append('four')
data_list.append('five')
data_list.append('six')
data_list.append('seven')
data_list.append('eight')
data_list.append('nine')
data_list.append('ten')

# 큐에 데이터 삽입, 큐가 꽉 차있다면 pass
for data in data_list:
        q.put_nowait(data)

# 큐에 넣은 데이터 확인, 큐가 비어있다면 pass
while q.qsize():
        print(q.get_nowait())  # one, two ~ nine, ten 순서대로 출력
```


