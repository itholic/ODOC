# 코루틴(co-routine)

자, 일반적인 함수는 다음과 같다

```python
def func():
    return 1
    
a = func()  # 함수에 진입하고, return 구문을 만나 값을 반환하고 종료
a  # 1
```

함수가 호출되면, 자신의 기능을 수행하고 값을 리턴후 종료된다.

하지만 파이썬에는 yield라는 문이 있어서, 함수가 값을 리턴하고 종료하는 대신 generator라는 객체를 반환해 마지막 yield문을 모두 소진할 때까지 계속 사용할 수 있게 해준다.


```python
def func():
    for i in range(5):
        yield i
        
f = func()  # generator 객체 반환
f.next()  # 0
f.next()  # 1
f.next()  # 2
f.next()  # 3
f.next()  # 4
f.next()  # yield 모두 소진시, StopIteration 예외 발생

```

즉, 함수 호출 후에 사라지는게 아니라, 함수 호출 후 다른 짓(?)을 하다가 함수의 다음 값이 필요할때 next()를 사용해서 원하는 값을 불러올 수 있다.

근데 여기서 끝이 아니라, 심지어 코루틴에게 값을 넘길수도 있다.


```python
def func(data):
    while True:
        val = yield data
        if val is not None:
            data += val
        
f = func(5)  # generator 객체 반환, data = 5
f.next()  # 5 반환후, 다음 yield 대기
f.send(10)  # data += 10 실행 후, 15 반환, 다음 yield 대기
f.send(4)  # data += 4 실행 후, 19 반환, 다음 yield 대기
f.next()  # 19 반환
```

즉, 한 번 호출되고 사라지는 것이 아닌, 그 값을 계속 Iterable하게 사용할 수 있으며, 심지어 메인루틴과 데이터를 주고받는 것 까지 가능하다.

이렇듯, 메인 루틴에 의해 일방적인 지시를 받고 사라지는 서브루틴과 달리 거의 동등한 협력(COoperation)관계를 이루기 때문에 CO-routine이라는 이름이 붙지 않았을까?
