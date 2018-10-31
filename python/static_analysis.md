# 파이썬 정적분석 

파이썬의 정적분석을 위한 모듈 두 가지를 소개한다.

정적분석이란, 프로그램을 돌리지 않고 코드 자체의 컨벤션이나 비효율적인 부분을 검사하는 것이다.

예를들어 선언하고 사용하지 않아서 메모리를 낭비하는 변수나,

변수 컨벤션을 지키지 않아 가독성을 저해할 수 있는 부분을 검사하는 것이다.

이러한 정적 분석을 사람의 눈으로 일일이 수행해도 되지만, 파일이 커질수록 한계가 있다.

이를 편하게 하기 위한 정적 분석 툴이 언어마다 존재하며, 파이썬에도 물론 존재한다.


## 1. pylint

pip으로 쉽게 설치할 수 있는 모듈이다

```
pip install pylint
```

사용도 간단하다

우선 정적분석할 파일을 만든다.

```python
# python_file.py
# -*- coding:utf-8 -*-

def test(msg):
    a = 0
    b = 10
    msg = msg
    def test_inner():
        return msg

    return test_inner

msg = "hello"
ti = test(msg)  # test_inner 함수 반환
print(ti())  # hello
```

test 함수는 특정 메시지를 매개변수로 전달하면, 내부 함수인 test_inner를 반환한다.

리턴받은 test_inner 함수를 통해 사용자가 전달한 메시지를 출력하는 함수이다.

실행하면 hello라는 문자열이 잘 출력된다.

그럼 이번엔 정적분석을 해볼까?

다음과 같이 -m 옵션을 주어 pylint를 지정 후, 정적분석할 파일경로를 적어주면 된다.

```
python -m pylint python_file.py
```

결과를 보자

```
python_file.py:1:0: C0111: Missing module docstring (missing-docstring)
python_file.py:3:0: C0111: Missing function docstring (missing-docstring)
python_file.py:3:9: W0621: Redefining name 'msg' from outer scope (line 12) (redefined-outer-name)
python_file.py:4:4: C0103: Variable name "a" doesn't conform to snake_case naming style (invalid-name)
python_file.py:5:4: C0103: Variable name "b" doesn't conform to snake_case naming style (invalid-name)
python_file.py:4:4: W0612: Unused variable 'a' (unused-variable)
python_file.py:5:4: W0612: Unused variable 'b' (unused-variable)
python_file.py:12:0: C0103: Constant name "msg" doesn't conform to UPPER_CASE naming style (invalid-name)
python_file.py:13:0: C0103: Constant name "ti" doesn't conform to UPPER_CASE naming style (invalid-name)

-------------------------------------------------------------------
Your code has been rated at 1.00/10 (previous run: -1.11/10, +2.11)
```

실행은 잘만 됐었는데, 정적 분석을 9 가지 개선 권고사항이 나왔다.

하나씩 지워나가보자.

우선 첫째줄과 둘재쭐은 모듈과 함수의 docstring(설명)이 빠졌다는 것이다.

docstring을 추가해주자.

```python
"""pylint 테스트를 위한 파일 """
# python_file.py
# -*- coding:utf-8 -*-

def test(msg):
    """ 내부함수를 반환하는 간단한 함수 """
    a = 0
    b = 10
    msg = msg
    def test_inner():
        return msg

    return test_inner

msg = "hello"
ti = test(msg)
print(ti())
```

다시 정적테스트를 돌려보자.

```
python_file.py:5:9: W0621: Redefining name 'msg' from outer scope (line 15) (redefined-outer-name)
python_file.py:7:4: C0103: Variable name "a" doesn't conform to snake_case naming style (invalid-name)
python_file.py:8:4: C0103: Variable name "b" doesn't conform to snake_case naming style (invalid-name)
python_file.py:7:4: W0612: Unused variable 'a' (unused-variable)
python_file.py:8:4: W0612: Unused variable 'b' (unused-variable)
python_file.py:15:0: C0103: Constant name "msg" doesn't conform to UPPER_CASE naming style (invalid-name)
python_file.py:16:0: C0103: Constant name "ti" doesn't conform to UPPER_CASE naming style (invalid-name)

------------------------------------------------------------------
Your code has been rated at 3.00/10 (previous run: 3.00/10, +0.00)
```

docstring을 추가해주니, 해당 부분에 대한 권고사항(?)이 사라졌다.

그 다음으로는 함수 안에서 선언된 'msg'라는 변수가 함수 바깥에서도 똑같이 사용된다는 점을 지적했다.

확실히 scope가 달라서 에러가 나진 않더라도,  프로그램이 커지면 같은 변수명을 사용하는 것은 혼란을 가져올 수 있다.

a, b 라는 변수는 lower_case 의 형태로 작성되는 것이 좋을 것 같다는 내용도 보인다. (한글자 변수는 인식이 어렵기 때문에 그런 것 같다)

사용하지 않는 변수 a, b가 존재한다고 한다. 이는 분명히 메모리의 낭비이다.

msg 라는 변수와 ti라는 변수는 상수같은데, 대문자로 명명하지 않았다는 내용도 보인다.

msg는 그렇다 쳐도, ti를 상수로 사용할 의도로 선언한 것은 아니므로 이쪽 권고는 무시하도록 하겠다.

정적분석 결과로 나오는 모든 권고사항을 다 수정할 필요는 없다.

파이썬 컨벤션에는 맞지만 프로젝트의 컨벤션에는 어긋나거나,  

프로그래머의 의도와 맞지 않은 권고사항은 알아서 걸러내면 된다.

(말그대로 이것은 표준 파이썬 문법을 기준으로 한 '권고사항'이다)

어쨌든 몇 가지 권고사항을 반영해보자.

```python
"""pylint 테스트를 위한 파일 """
# python_file.py
# -*- coding:utf-8 -*-

def test(msg):
    """ 내부함수를 반환하는 간단한 함수 """
    msg = msg
    def test_inner():
        return msg

    return test_inner

MESSAGE = "hello"
ti = test(MESSAGE)
print(ti())
```

정적 분석을 마치고 나니 필요없는 코드도 사라지고, 목적별로 적절한 컨벤션을 적용하여 보다 깔끔해졌다.

성능적으로도 메모리 낭비를 줄이고, docstring을 추가함으로써 코드의 가독성 또한 한결 나아졌다.

마지막으로 한 번 정적분석을 다시 돌려보자.

```
python_file.py:14:0: C0103: Constant name "ti" doesn't conform to UPPER_CASE naming style (invalid-name)

------------------------------------------------------------------
Your code has been rated at 8.75/10 (previous run: 2.50/10, +6.25)
```

아직 권고사항 한 개가 남아있는데,

'ti'는 test함수의 return값을 받기위한 변수로, 상수로 사용할 의도가 없기때문에 굳이 대문자로 바꾸지 않았다.

밑에 나오는 rate는 아마 pylint가 권고하는 정적분석 컨벤션을 기준으로 해당 코드는 몇 점 정도에 해당하는지 보여주는 것 같다.


## 2. flake8

flake8 또한 pip으로 간편하게 설치해서 사용할 수 있는 파이썬 정적분석 도구이다.

```
pip install flake8
```

pylint와 동일하게 사용하면 된다.

수정되기 전 초기상태의 코드에 flake8을 이용해 정적분석을 돌려보자.

```
# python_file.py
# -*- coding:utf-8 -*-

def test(msg):
    a = 0
    b = 10
    msg = msg
    def test_inner():
        return msg

    return test_inner

msg = "hello"
ti = test(msg)  # test_inner 함수 반환
print(ti())  # hello
```

```
python -m flake8 python_file.py
```

결과는 다음과 같다.

```
python_file.py:4:1: E302 expected 2 blank lines, found 1
python_file.py:5:5: F841 local variable 'a' is assigned to but never used
python_file.py:6:5: F841 local variable 'b' is assigned to but never used
python_file.py:8:5: E306 expected 1 blank line before a nested definition, found 0
python_file.py:13:1: E305 expected 2 blank lines after class or function definition, found 1
```

pylint와는 조금 다른 결과가 나왔다.

우선 docstring에 대한 권고가 나오지 않았으며, 상수로 사용하는 변수와 관련한 권고도 나오지 않았다.

다만, 첫 번째 라인은 2줄의 공백을 넣어준 후 시작하라는 권고와,

내부 함수를 선언하기 이전에 한 줄의 공백을 넣으라는 권고,

그리고 클래스나 함수의 선언 이후 2줄의 공백을 넣으라는 권고가 추가됐다.

그리고 사용하지 않는 변수에 대한 권고는 pylint와 동일하게 출력됐다.

수정해보자.

```python
# python_file.py
# -*- coding:utf-8 -*-


def test(msg):
    msg = msg

    def test_inner():
        return msg

    return test_inner


msg = "hello"
ti = test(msg)  # test_inner 함수 반환
print(ti())  # hello
```

미세한 차이지만, 

def test(msg)가 시작되는 부분 위쪽에 두 줄의 공백을 주었고,

내부 함수인 test_inner()가 시작되는 부분 위쪽에 한 줄의 공백,

그리고 def test(msg)의 정의가 끝나고 msg = "hello"를 선언하는 부분 위쪽에 두 줄의 공백을 주었다.

마지막으로 사용하지 않는 변수 a, b를 지워주었다.

정적분석을 다시 돌려보자.

```
python -m flake8 python_file.py
```

모든 권고사항을 수정했으므로 아무 결과도 나오지 않는다. 

## 3. 결론

파이썬에는 pylint, klake8등의 정적분석 도구가 존재한다. 

다른 분석 도구가 더 있을수도 있고, 사용자가 직접 만들어서 사용할수도 있다.

정적 분석 도구는 사람이 일일이 확인하기 어려운 코드상 개선사항을 자동으로 찾아주지만,

본인이 참여한 프로젝트의 컨벤션이나 프로그래머의 의도와 맞지 않은 개선사항을 권고하기도 한다.

따라서 이러한 정적 분석 도구를 잘 활용하면 코드 품질을 빠르게 개선시킬 수 있지만,

상황에 따라 적절한 분석 도구를 선택할줄 알아야하며, 개선사항을 개발자 스스로 잘 걸러내어 적용할 수 있어야한다.
