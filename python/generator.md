# generator


generator는 얼핏 함수와 비슷하지만, 호출시 generator 객체를 반환한다.

generator 객체는 Iterable하며, next() 메소드를 통해 다음 yield 값을 리턴한다.

리턴할 yield 값이 떨어지면 StopIteration 예외를 발생시킨다.

말로만 하면 이해가 안되니 코드를 보자.

```python
# -*- coding:utf-8 -*-


def generator():
    yield 10

gen = generator() 
print gen  # generator 객체
print 'generator'
print gen.next()  # 10
#print gen.next()  # StopIteration

def generator_many(cnt):
    while cnt != 0:
        yield cnt
        cnt -= 1

gen = generator_many(5)
print 'generator_many'
print gen.next()  # 5
print gen.next()  # 4
print gen.next()  # 3
print gen.next()  # 2
print gen.next()  # 1
#print gen.next()  # StopIteration
    

# generator로 값을 넘겨주는 것 또한 가능하다. 
# send(data) 시, yield를 받는 변수에 값을 넘기고, next()가 자동으로 실행된다.
def generator_send():
    while True:
        receive = yield 10
        print receive

gen = generator_send()
print 'generator_send'
#print gen.send('hi')  # 객체를 생성하자마자 send는 불가능.
print gen.next()  # 10
print gen.next()  # None \n 10
print gen.send('hi')  # hi \n 10


# close() 메소드를 통해 종료 가능하며, GeneratorExit 예외를 반환한다.

"""이런식으로 함수가 한 번 호출후 바로 사라지지 않고 계속 살아있으면서,
메인루틴과 지속적인 협력관계를 유지하는 루틴을 coroutine이라고 한다.
"""
```
