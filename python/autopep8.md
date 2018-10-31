# autopep8

autopep8은 그 이름을 보면 짐작할 수 있듯,

파이썬 코드를 PEP8 컨벤션에 맞게 자동으로 교정해주는 모듈이다.

앞서 정리한 <a href="https://itholic.github.io/python-static-analysis/" target="_blank">정적 분석</a>에 포함시키려다가 따로 정리했다.

왜냐면 autopep8은 엄밀히 따져서 정적분석은 아니고, 단지 PEP8 컨벤션에 맞추어주는 모듈이기 때문이다.

예를들면 사용하지 않거나 중복 선언된 변수 등을 잡아주지는 않는다.

코드의 '모양' 자체를 PEP8에 맞도록 맞추어주는 것이다.

예를 들어 다음과 같은 코드가 있다.

```python
# python_file.py
# -*- coding:utf-8 -*-
def test(msg):
    a = 10
    b = 50
    msg =                msg
    def test_inner():
        return msg
    return test_inner
msg = "hello"
ti = test(msg)  # test_inner 함수 반환
print(ti())  # hello
```

이를 pylint나 flake8같은 모듈을 통해 정적 분석을 하면, 

'a', 'b'처럼 선언만되고 실제로 사용되지 않는 변수나, 

'msg'처럼 서로 다른 namespace에서 같은 이름으로 선언된 변수에 대한 수정 권고사항을 준다.

하지만 autopep8은 단순히 '코드의 전체적인 모양'을 PEP8과 최대한 비슷하게 맞추어준다.


사실 이 모듈을 사용하는 것 자체를 그렇게 권고하지는 않기 때문에 정리하지 않으려 했으나,

그래도 편리한 부분이 있고, 잘 활용하기 나름이기때문에 일단 정리한다.

어쨌든 한 번 사용해보자.

우선 설치를 해야한다.

```
pip install autopep8
```

사용해보자.

```
python -m autopep8 python_file.py
```

결과는 다음과 같다.

```python
# python_file.py
# -*- coding:utf-8 -*-


def test(msg):
    a = 10
    b = 100
    msg = msg

    def test_inner():
        return msg
    return test_inner


msg = "hello"
ti = test(msg)  # test_inner 함수 반환
print(ti())  # hello
```

말그대로 전체적인 모양을 PEP8에 맞추어 줬을 뿐,

코드 스타일이나 warning같은 권고사항을 주지는 않는다.

그리고 사실 PEP8에서 권유하는 사항을 다 잡아주지도 못한다.

예를 들면 함수명과 변수명을 lower_case로 한다던지 하는 부분들을 말하는 것이다.

변수명을 CamelCase로 작성하더라도 autopep8은 그것까지 잡아내진 못한다.

어쨌든 autopep8은 유용한 면이 있다.

정적 분석을 모두 마치고, 미처 잡아내지 못한 부분에서 코드를 좀 더 깔끔하게 정리하는 목적으로는 훌륭하다.

하지만 코딩을 할 때에는 PEP8을 신경쓰지 않다가,

마지막에 autopep8을 사용해 코드를 정리하는 용도로 사용한다면 비추천한다.

일단 근본적으로 PEP8은 단지 모양 맞추기 놀이가 아니다.

좀 더 깔끔하고 가독성있는 코드를 만들어 결국 생산성과 유지보수성을 높이고,

'Pythonic'이라는 철학에 한 걸음 가까워지는데 그 의의가 있다고 생각한다.

너무 깊이 들어간 것 같다. 

어쨌든 autopep8을 적절히 잘 활용하되, 

스스로도 PEP8 컨벤션을 잘 맞추도록 신경쓰고, 

그 안에서 파이썬이 제시하는 철학을 잘 배워나갔으면 좋겠다.

물론 나 또한 많이 배워나가야 할 부분이다.
