# 동일성 vs 동등성

파이썬에서는 값을 비교하는 두 가지 방법이 있다.

하나는 'is'를 통한 동일성(Identity) 비교,

하나는 '=='을 통한 동등성(Equality) 비교이다.

말로하면 헷갈리는데, 다음 예제를 보면 한 번에 이해가 가능할 것이다.

```python
def return_1000():
    return 1000
    
def return_thousand():
    return 1000
    
a = return_1000()
b = return_thousand()

print(a)  # 1000
print(b)  # 1000

print(id(a))  # 35920704
print(id(b))  # 35920728

print(a is b)  # False
print(a == b)  # True
```

return_1000 함수와 return_thousand 함수 둘 다 숫자 '1000'을 반환하는 함수이다.

그래서 단순히 값을 출력해보면 당연히 둘 다 1000이 출력된다.

**하지만 객체의 고유 값(identity)을 출력하는 'id' 함수를 통해 출력해보면 서로 다른 값이 출력된다.**

이는 return_1000 함수가 '1000'이라는 값을 반환할 때 할당한 메모리 공간과

return_thousand 함수가 '1000'이라는 값을 반환할때 할당한 메모리 공간이 서로 다르기 때문이다.

그 결과로,

'is'를 이용해 비교할 때에는 False가 반환되고,

'=='을 이용해 비교할 때에는 True가 반환되었다.

둘다 값은 똑같이 1000이지만, 

**is를 통한 비교는 그 객체가 할당된 메모리 공간까지 완전히 동일한지를 비교하는 것이다.**

이 테스트로 내릴 수 있는 결론은 심플하다.

1. 두 객체가 id(메모리 공간)까지 완전히 동일한지를 비교하려면 is 비교.
2. 두 객체가 단순히 가지고 있는 값만 동일한지 비교하려면 == 비교.

'동일성'이니 '동등성'이니 복잡한 말은 사용하지 말자.

그런데 파이썬에서는 None이나 True, False 같은 객체들은 어떤 공간에서 선언하든 항상 똑같은 메모리 공간에 할당한다.

더 정확히 말하면,

몇몇 특정한 객체들은 최초 선언시 딱 한 번만 메모리에 할당하고,

그 이후에 선언되는 값들은 모두 최초 할당된 메모리 공간을 가리키도록 한다.

...

그냥 예제를 보자.

```python
def return_true():
    return True
    
def return_not_false():
    return not False
    
a = return_true()
b = return_not_false()

print(a)  # True
print(b)  # True

print(id(a))  # 140270577998592
print(id(b))  # 140270577998592

print(a is b)  # True
print(a == b)  # True
```

return_true 함수는 True를 반환하고,

return_not_false 함수는 not False, 즉, 마찬가지로 True를 반환한다.

print를 찍어보면 당연히 둘 다 True인데,

첫 번째 예제와 다른 점은 id 값도 똑같다는 점이다.

**이 id값은 프로그램을 다시 실행할 때마다 바뀌지만, a와 b의 id가 항상 같은 것은 변함이 없다.**

즉, 최초 선언시 한 번만 메모리에 할당하고, 그 이후에는 최초에 선언된 값을 그대로 사용하도록 하는 것이다.

첫 번째 예제에서 '1000'을 선언할 때에는, 선언할 때마다 다른 메모리 공간을 할당해서 id가 달랐었다.

그래서 True, False 같은 값들은 'is'로 비교하든 '=='로 비교하든 상관이 없다.

**※단!**

이러한 값들은 무조건 is로 비교하는 것이 성능상 이득이며, 파이썬에서도 권고하는 방식이다.(PEP8)

피부로 느끼기 위해 비교해보자.

```python
from datetime import datetime

a = True

start = datetime.now()
for _ in range(10000000):
    a is True
print ("is perfomance : {}".format(datetime.now() - start))

start = datetime.now()
for _ in range(10000000):
    a == True
print ("== perfomance : {}".format( datetime.now() - start))
```

'is'로 값 비교를 1천만번 수행해서 시간을 측정하고,

'=='로 값 비교를 1천만번 수행해서 시간을 측정했다.

5번 수행한 결과는 다음과 같다.

```
is perfomance : 0:00:03.993514
== perfomance : 0:00:04.202176

is perfomance : 0:00:04.013707
== perfomance : 0:00:04.166339

is perfomance : 0:00:04.002838
== perfomance : 0:00:04.196119

is perfomance : 0:00:04.001575
== perfomance : 0:00:04.193248

is perfomance : 0:00:04.035875
== perfomance : 0:00:04.128455
```

미세하지만 is로 비교하는 것이 확실한 성능적 우위를 보인다.

이는 매우 단순한 테스트이기 때문에 큰 차이라고 느끼지 못할 수도 있지만,

실제로 프로그램의 성능을 단 0.1초라도 줄이는 것은 엄청난 성과이다.

그러니 is로 비교할 수 있는 상황에서는 반드시 is 비교를 쓰도록 하자.

그렇다고 is 비교를 남발하지 말고,

상황을 잘 판단해 값을 단순 비교 할때에는 '==' 비교를 써서 오류가 발생하지 않도록 하자.

실제로도 is 비교보다는 웬만한 상황에서는 '==' 비교를 사용하는 상황이 더 많다.
