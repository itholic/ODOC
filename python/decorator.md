# 데코레이터

데코레이터의 이름만 보면 뭔가를 '꾸며주는' 역할을 할 것 같다.

파이썬에서 데코레이터는 함수를 꾸며주는 역할을 한다.

기존에 정의해놓은 함수에 뭔가 추가 기능을 더하고싶을때 데코레이터를 사용하면 편리하다.

예제를 보자.

```python
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        return "cannot divide by 0"


add(3, 4)  # 7
sub(3, 4)  # -1
mul(3, 4)  # 12
div(3, 4)  # 0.75
```

간단한 사칙연산 함수 4개를 정의했다.

그런데, 사칙연산 함수에 다음과 같은 기능을 넣고싶어졌다.

1. 실행되는 함수명 출력
2. 함수가 실행될때 인자로 넘어온 값 출력


다음과 같이 해주면 될것이다.

```python
def add(a, b):
    print ('func name : {}'.format(add.__name__))
    print ('first arg : {}'.format(a))
    print ('second arg : {}'.format(b))
    return a + b


def sub(a, b):
    print ('func name : {}'.format(sub.__name__))
    print ('first arg : {}'.format(a))
    print ('second arg : {}'.format(b))
    return a - b


def mul(a, b):
    print ('func name : {}'.format(mul.__name__))
    print ('first arg : {}'.format(a))
    print ('second arg : {}'.format(b))
    return a * b


def div(a, b):
    print ('func name : {}'.format(div.__name__))
    print ('first arg : {}'.format(a))
    print ('second arg : {}'.format(b))
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        return "cannot divide by 0"


add(3, 4)  # func name : add \n first arg : 3 \n second arg : 4
sub(3, 4)  # func name : sub \n first arg : 3 \n second arg : 4
mul(3, 4)  # func name : mul \n first arg : 3 \n second arg : 4
div(3, 4)  # func name : div \n first arg : 3 \n second arg : 4
```

처리하긴 했는데 어째 뭔가 찝찝하다.

중복되는 부분이 너무 많다.

그리고 모든 함수를 일일이 다 수정해주어야 하는 번거로움이 있다.

해당 예제에서는 간단한 함수를 예로 들었고 4개밖에 되지 않지만,

함수가 복잡해지고 수십, 수백개의 함수에 대해 동일한 기능을 추가한다고 생각하면 어떨까?

<br/>

바로 이런 상황을 간단히 처리하기 위해 데코레이터라는 기능이 존재한다.

데코레이터를 이해하기 위해서는 우선 <a href="https://itholic.github.io/etc-first-class-citizen/" target="_blank">[일급 객체]</a>와 <a href="https://itholic.github.io/python-closure/" target="_blank">[클로저]</a>의 개념을 어느정도 알고있는것이 좋다.

대괄호로 표시한 부분에 이전 포스팅 링크를 걸어놓았으니 참고하면 될 것 같다.

<br/>

물론 이러한 개념을 몰라도 대강 동작 방식을 익히는데는 무리가 없지만,

단순히 사용하는 것과 정확히 이해하고 응용하는 것은 차이가 크다고 생각한다.

<br/>

어쨌든, 파이썬에서 함수는 일급 객체이기 때문에 다른 함수의 인자로 넘길수있다.

이 특징을 이용해 위의 코드를 다음과 같이 바꿀 수 있다.

```python
def print_name_and_args(func, a, b):
    print ('func name : {}'.format(func.__name__))
    print ('first arg : {}'.format(a))
    print ('second arg : {}'.format(b))
    return func(a, b)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        return "cannot divide by 0"


print_name_and_args(add, 3, 4)
print_name_and_args(sub, 3, 4)
print_name_and_args(mul, 3, 4)
print_name_and_args(div, 3, 4)
```

함수명과 인자값을 출력하는부분을 print_name_ang_args 라는 함수로 따로 만들고,

인자로 함수명과 함수를 실행시키는데 필요한 인자를 받도록 했다.

<br/>

그런데 이렇게 하면 단점이 하나 있다.

실제로 함수를 실행시킬때 `print_name_and_args(add, 3, 4)` 와 같이 복잡하게 사용해야한다.

그냥 단순히 `add(3, 4)`처럼 쓰는것이 훨씬 편하지 않겠는가?

다음과 같이 코드를 바꿔보자.

```python
def print_name_and_args(func):
    func = func
    
    def wrapper(a, b):
        print ('func name : {}'.format(func.__name__))
        print ('first arg : {}'.format(a))
        print ('second arg : {}'.format(b))
        return func(a, b)
    return wrapper


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        return "cannot divide by 0"


add = print_name_and_args(add)  # wrapper 함수 반환
sub = print_name_and_args(sub)  # wrapper 함수 반환
mul = print_name_and_args(mul)  # wrapper 함수 반환
div = print_name_and_args(div)  # wrapper 함수 반환

add(3, 4)  # 원래 원하던 함수 호출 모양
sub(3, 4)
mul(3, 4)
div(3, 4)
```

print_name_and_args를 통해 바로 함수를 호출하지 않고,

wrapper 함수를 만들어 그 안에다가 원하는 기능을 추가 한 후에, wrapper 함수 자체를 리턴해줬다.

최종적으로 뭔가 좀 복잡해지긴 했지만,

어쨌든 결국엔 맨 처음 구현했던 모양대로 함수를 호출했다.

<br/>

함수를 다른 함수의 return 값으로 사용할 수 있다는 일급 객체의 특징과,

리턴된 내부함수가 외부함수의 프리변수를 사용할 수 있다는 클로저의 특징을 활용했다.

그래서 print_name_and_args 함수의 리턴값으로 wrapper 함수 자체를 반환했고,

반환된 wrapper 함수를 변수에 넣어놨다가 외부함수의 변수인 func를 사용해 최종적으로 함수를 실행시켰다.

<br/>

근데 이것도 뭔가 불편하다.

사용 할때마다 일일이 print_name_and_args 함수를 호출해 wrapper를 변수에 할당하고,

할당된 wrapper를 통해 다시 함수를 호출해주어야 한다.

마지막으로 다음과 같이 바꿔보자.

```python
def print_name_and_args(func):
    func = func
    
    def wrapper(a, b):
        print ('func name : {}'.format(func.__name__))
        print ('first arg : {}'.format(a))
        print ('second arg : {}'.format(b))
        return func(a, b)
    return wrapper


@print_name_and_args
def add(a, b):
    return a + b


@print_name_and_args
def sub(a, b):
    return a - b


@print_name_and_args
def mul(a, b):
    return a * b


@print_name_and_args
def div(a, b):
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        return "cannot divide by 0"


add(3, 4)
sub(3, 4)
mul(3, 4)
div(3, 4)
```

print_name_and_args 함수를 적용하고자 하는 함수들의 머리(?) 부분에 @print_name_and_args 라는 코드를 추가했다.

그랬더니 해당 함수가 print_name_and_args 함수의 인자로 자동으로 넘어가면서, wrapper 함수의 실행까지 자동으로 이루어진다.

이 때, print_name_and_args 함수를 데코레이터라고 한다.

그리고 데코레이터를 기존 함수에 적용하고 싶을 때에는,

해당 함수의 머리에 `@데코레이터이름` 을 적어주면 된다.

<br/>

근데, 지금은 인자를 두 개 받는 함수에 한해서만 데코레이터가 동작한다.

다음과 같이 인자를 세 개 받는 함수에 print_name_and_args 데코레이터를 적용한다면 어떻게 될까?

```python
def print_name_and_args(func):
    func = func
    
    def wrapper(a, b):
        print ('func name : {}'.format(func.__name__))
        print ('first arg : {}'.format(a))
        print ('second arg : {}'.format(b))
        return func(a, b)
    return wrapper


@print_name_and_args
def add_three(a, b, c):
    return a + b  + c


add_three(1, 2, 3)
```

실행하면 다음과 같은 에러를 볼 수 있다.

```
Traceback (most recent call last):
  File "D:/git_store/testdir/deco.py", line 15, in <module>
    print add_three(1, 2, 3)
TypeError: wrapper() takes exactly 2 arguments (3 given)
```

wrapper 함수는 2개의 인자만을 받는데,

데코레이터로 넘겨준 add_three는 세 개의 변수를 받고있기 때문이다.

데코레이터의 wrapper에서 여러 인자를 받을 수 있도록 바꾸어보자.

```python
def print_name_and_args(func):
    func = func
    
    def wrapper(*args):
        if len(args) == 2:
            print ('func name : {}'.format(func.__name__))
            print ('first arg : {}'.format(args[0]))
            print ('second arg : {}'.format(args[1]))
        elif len(args) == 3:
            print ('func name : {}'.format(func.__name__))
            print ('first arg : {}'.format(args[0]))
            print ('second arg : {}'.format(args[1]))
            print ('third arg : {}'.format(args[2]))
        return func(*args)
    return wrapper


@print_name_and_args
def add_three(a, b, c):
    return a + b  + c


add_three(1, 2, 3)  # func name : add_three \n first arg : 1 \n second arg : 2 \n third arg : 3
```

고정 변수대신 가변길이 변수를 받을 수 있도록 * 키워드를 사용했다.

그리고 변수의 갯수에 따라 분기를 나누어 각각 다른 처리를 해주었다.

<br/>

하지만 이렇게하면 변수의 갯수마다 분기를 추가해야하므로,

굳이 first, second, third 라는 키워드를 쓰지 않고 다음과 같이 한 번에 처리하는게 더 깔끔할 것 같다.

```python
def print_name_and_args(func):
    func = func
    
    def wrapper(*args):
        print ('func name : {}'.format(func.__name__))
        print ('args : {}'.format(args))
        return func(*args)
    return wrapper


@print_name_and_args
def add_three(a, b, c):
    return a + b  + c
    
    
add_three(1, 2, 3)  # func name : add_three \n args : (1, 2, 3)
```

마지막으로 전체 코드를 보자.

```python
def print_name_and_args(func):
    func = func
    
    def wrapper(*args):
        print ('func name : {}'.format(func.__name__))
        print ('args : {}'.format(args))
        return func(*args)
    return wrapper


@print_name_and_args
def add(a, b):
    return a + b


@print_name_and_args
def sub(a, b):
    return a - b


@print_name_and_args
def mul(a, b):
    return a * b


@print_name_and_args
def div(a, b):
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        return "cannot divide by 0"


@print_name_and_args
def add_three(a, b, c):
    return a + b  + c


add(3, 4)  # func name : add \n args : (3, 4)
sub(3, 4)  # func name : sub \n args : (3, 4)
mul(3, 4)  # func name : mul \n args : (3, 4)
div(3, 4)  # func name : div \n args : (3, 4)
add_three(1, 2, 3)  # func name : add_three \n args : (1, 2, 3)
```

print_name_and_args 라는 데코레이터를 정의해서,

@print_name_and_args 라는 단 한줄의 코드를 통해,

서로 다른 변수를 받는 모든 함수에 같은 기능을 손쉽게 추가했다.


## 데코레이터 추가

그런데, 이 상태에서 함수의 시작 시간을 알려주는 데코레이터를 추가하고 싶을 수도 있다.

```python
import datetime

def print_name_and_args(func):
    func = func
    
    def wrapper(*args):
        print ("{} is started at {}".format(func.__name__, datetime.datetime.now()))  # 단순히 한 줄 추가
        print ('func name : {}'.format(func.__name__))
        print ('args : {}'.format(args))
        return func(*args)
    return wrapper
```

물론 현재 상황에서는 위와 같이 기존 데코레이터에 간단히 한 줄을 추가하는게 더 빠르지만,

예시를 위해 다음과 같이 print_start_time이라는 데코레이터를 하나 더 만들어서 추가한다고 가정하자.

```python
import datetime

def print_name_and_args(func):
    """ print func name and args """
    func = func
    
    def wrapper(*args):
        print ('func name : {}'.format(func.__name__))
        print ('args : {}'.format(args))
        return func(*args)
    return wrapper


def print_start_time(func):
    """ print start time """
    func = func
    
    def wrapper(*args):
        print ("{} is started at {}".format(func.__name__, datetime.datetime.now()))
        return func(*args)
    return wrapper
```

이제 단순히 다음과 같이 사용하면 된다.

```python
import datetime

def print_name_and_args(func):
    """ print func name and args """
    func = func  # 3. 'add' 함수가 아닌 'wrapper' 함수를 받음
    
    def wrapper(*args):
        print ('func name : {}'.format(func.__name__))  # 4. 함수명이 'wrapper'로 출력됨
        print ('args : {}'.format(args))
        return func(*args)
    return wrapper


def print_start_time(func):
    """ print start time """
    func = func
    
    def wrapper(*args):
        print ("{} is started at {}".format(func.__name__, datetime.datetime.now()))
        return func(*args)
    return wrapper  # 2. print_name_and_args 데코레이터에 wrapper 함수 리턴


# 사용할 데코레이터 추가 선언
@print_name_and_args
@print_start_time  # 1. 먼저 실행
def add(a, b):
    return a + b


add(3, 4)
```

단순히 기존 데코레이터 선언부에 @print_start_time 한 줄을 추가해 주었다.

추가된 주석은 무시하고 실행 결과를 먼저 보자.

```
func name : wrapper
args : (3, 4)
add is started at 2018-11-10 14:37:53.360000
7
```

함수명과 받은 인자, 그리고 시작 시간이 출력됐다.

근데 이상한 점이 있다.

함수명이 'add'가 아닌 'wrapper'라고 출력되었다.

왜 그럴까?

<br/>

주석에 매겨놓은 번호를 1번부터 순서대로 따라가보자.

데코레이터를 중첩해서 사용시,

1. add 함수 바로 위쪽에 선언된 print_start_time이 먼저 실행된다.

2. print_start_time은 print_name_and_args쪽으로 함수를 return 하는데, 
이 때 'add' 함수가 아닌 'wrapper' 함수를 리턴하는 것을 볼 수 있다.

3. print_name_and_args 데코레이터는 'wrapper' 함수를 받았기 때문에,

4. 함수명 출력시 'wrapper'가 출력되는 것이다.

<br/>

이는 다음과 같이 functools 모듈의 wraps 라는 기능으로 간단히 해결할 수 있다.

```python
import datetime
from functools import wraps

def print_name_and_args(func):
    """ print func name and args """
    func = func
    
    @wraps(func)
    def wrapper(*args):
        print ('func name : {}'.format(func.__name__))
        print ('args : {}'.format(args))
        return func(*args)
    return wrapper


def print_start_time(func):
    """ print start time """
    func = func
    
    @wraps(func)
    def wrapper(*args):
        print ("{} is started at {}".format(func.__name__, datetime.datetime.now()))
        return func(*args)
    return wrapper


@print_name_and_args
@print_start_time
def add(a, b):
    return a + b


add(3, 4)
```

각 데코레이터의 wrapper 함수 위쪽에 @wraps 라는 구문을 추가해주면 된다.

참고로 모양을 보면알겠지만, wraps 또한 functools에서 정의해놓은 데코레이터이다.

실행하면 다음과 같이 정상적으로 함수명이 출력되는 것을 확인할 수 있다.

```
func name : add
args : (3, 4)
add is started at 2018-11-10 14:37:53.360000
7
```

## class 기반 데코레이터

지금은 print_name_and_args 라는 함수를 통해 데코레이터를 만들었는데,

클래스로 데코레이터를 만들수는 없을까?

다음과 같이 만들어주면 된다.

```python
class PrintNameAndArgs:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args):
        print ('func name : {}'.format(self.func.__name__))
        print ('args : {}'.format(args))
        return self.func(*args)


@PrintNameAndArgs
def add(a, b):
    return a + b


@PrintNameAndArgs
def sub(a, b):
    return a - b


@PrintNameAndArgs
def mul(a, b):
    return a * b


@PrintNameAndArgs
def div(a, b):
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        return "cannot divide by 0"


@PrintNameAndArgs
def add_three(a, b, c):
    return a + b  + c


add(3, 4)  # func name : add \n args : (3, 4)
sub(3, 4)  # func name : sub \n args : (3, 4)
mul(3, 4)  # func name : mul \n args : (3, 4)
div(3, 4)  # func name : div \n args : (3, 4)
add_three(1, 2, 3)  # func name : add_three \n args : (1, 2, 3)
```

클래스의 __call__ 함수에 추가 기능을 선언하고 return 해주면 된다.

하지만 실제로는 class 기반보다 함수 기반 데코레이터를 더 많이 쓴다고 하니 참고만 해두자.
