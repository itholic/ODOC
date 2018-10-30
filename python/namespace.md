# namespace

python에서는 변수의 유효 범위를 네임스페이스(namespace) 기반으로 결정한다

네임 스페이스는 Local, Enclosed, Global, Built-in 이 있으며, 이를 줄여 LEGB라 한다.

이는 변수를 확인할때 먼저 확인하는 순서이기도 하다.

- Local : 지역적 네임스페이스로, 클래스나 함수의 내부 범위
- Enclosed : 내부 함수에서 외부 함수의 변수를 사용할 수 있는 범위
- Global : 전역적 네임스페이스로, 파일 단위의 모듈 범위
- Built-in : 내장 네임스페이스로, 파이썬으로 작성된 모든 코드 범위


유의해야할 경우 몇 가지를 살펴보자.

### Global

우선 다음과 같이 Global 변수를 함수 내에서 읽어보자.

```python
# -*- coding:utf-8 -*-

g_num = 100

def test():
    return g_num

print test()  # 100
```

100이 출력되는 것으로 보아, test() 함수 내에서 글로벌 변수인 g_num에 접근 가능하다.

그럼 g_num을 바꿔볼까?

```python
# -*- coding:utf-8 -*-

g_num = 100

def test():
    g_num += 1
    return g_num

print test()  # UnboundLocalError: local variable 'g_num' referenced before assignment
```

g_num에 1을 더해서 101이라는 결과를 기대했는데 오류가 났다.

local 변수인 g_num을 선언하기 전에 접근했다는 것이다.

나는 global 변수인 g_num의 값을 1 더하고싶었을 뿐인데 왜 그럴까?

방법이 없을까?

없을리가 없다.

global 변수를 local 범위 안에서 사용 할 때에는 다음과 같이 해당 변수가 global 변수라는 것을 명시해주어야한다.

```python
# -*- coding:utf-8 -*-

g_num = 100

def test():
    global g_num  # global 변수 g_num을 사용하겠습니다
    g_num += 1
    return g_num

print test()  # 101
```

### Nonlocal

그럼 비슷한 개념으로,

다음과 같이 외부 함수의 변수를 내부 함수에서 사용하면 어떻게 될까?


```python
# -*- coding:utf-8 -*-

def outter():
	outter_int = 100
    
    def inner():
    	return outter_int

    print inner()
    
outter()  # 100
```

inner() 함수 에서 outter() 함수의 변수인 outter_int를 제대로 반환한 것을 확인할 수 있다.

그럼 앞선 예제와 마찬가지로, 값을 변경해서 반환해볼까?

```python
# -*- coding:utf-8 -*-

def outter():
	outter_int = 100
    
    def inner():
        outter_int += 1
    	return outter_int

    print inner()
    
outter()  # UnboundLocalError: local variable 'outter_int' referenced before assignment
```

앞선 예제와 같은 에러가 발생한다.

근데 outter_int는 global 변수가 아니라서 global 키워드로 해결하기는 어려워보인다.

이번엔 진짜로 방법이 없을까?

역시 방법이 없을리가 없다.

파이썬에서는 다음과 같이 nonlocal 키워드를 제공해, 내부 함수에서 외부 함수의 값을 수정 가능하도록 한다.

단, 이는 파이썬 3에서만 지원한다는 점을 명심하자.

```python
# -*- coding:utf-8 -*-

def outter():
	outter_int = 100
    
    def inner():
        nonlocal outter_int
        outter_int += 1
    	return outter_int

    print inner()
    
outter()  # 101
```

이때 잘 보면,

outter_int는 inner()함수의 입장에서 global변수도 아니고 local변수도 아니지만 사용하는데 무리가 없다.

이러한 변수를 프리 변수(free variable)라 한다.


### Variable Shadowing

마지막으로 Variable Shadowing에 대한 예제를 간단히 보고 마무리하자.

Variable Shadowing이란, 우선순위의 네임스페이스 변수에 의해 후순위 네임스페이스 변수가 가려지는 것이다.

말로하면 어려우니 예제를 보자.

```python
# -*- coding:utf-8 -*-

g_num = 100

def test():
    g_num = 50
    return g_num

print test()  # 50
print g_num  # 100
```

맨 처음에 봤던 예제다.

test() 함수 내에서 global 변수와 이름이 동일한 g_num을 선언하고 리턴했다.

그랬더니, global 변수의 값 100이 아닌 test() 내부에서 선언한 local 변수의 값 50이 반환됐다.

그리고 다시 함수 외부에서 g_num을 프린트해보니 global 값인 100이 나왔다.

즉, global 변수가 완전히 사라진 것은 아니고, 잠시 '가려진' 것이다.

맨 처음에 언급한 LEGB를 기억하는가?

앞에 나올수록 우선순위가 높다고 했다.

즉,

현재 local 변수에도 g_num이 있고, global 변수에도 g_num 이 있는데,

변수 네임스페이스 우선순위가 local(L)이 더 높으므로 local 변수의 값인 50이 출려되

이처럼 우선 순위의 네임스페이스에 의해 후순위의 네임스페이스 변수가 가려지는 것을 Variable Shadowing이라 한다.
