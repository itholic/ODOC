# PEP8

물론 동작하는 코드를 짜는 것도 중요하지만, 어찌보면 개발자에게 그건 당연한 문제이다.

단순히 동작하는 코드를 짜는 것 보다 중요한 것은 많다.

그 요소중 하나는 바로 코딩 컨벤션(규칙)을 지키는 것이며, 

PEP8은 python 코딩 컨벤션에 대해 기술하고 있다.

```python
# -*- coding:utf-8 -*-
"""프로젝트 내에서 선행되던 규칙이 있다면, 그 규칙이 우선이다.
* 실제 코딩시에는 주석을 영어로 쓰자 \
주석은 완전한 문장을 쓰며, 마지막은 마침표로 끝내자 \
주석의 시작은 대문자를 사용하자 \
마침표 뒤에는 두 칸의 공백을 준다.  

파이썬 코딩 컨벤션
일단, 한 줄의 문자 길이는 79자 이하여야 한다.
주석이나 DocString 의 경우는 72자까지 허용한다.
들여쓰기는 공백 4칸을 권장한다.(tap이 아닌 space 4번)

여러 개의 이항 연산자가 사용되는 문장의 경우에는
+ 이항 연산자의 앞쪽에서 줄바꿈을 하는 것을 더욱 권장한다.
+ 이는 가독성과 관련이 있으며,
+ 더욱 최신 표현법이기도 하다.

세 개의 따옴표를 사용할 때에는 반드시 쌍따옴표를 사용하자
"""
# 블록 주석은 뒤에 따라오는 코드에 대한 설명이며, 해당 코드와 indent를 맞춘다.
# 블록 주석은 모든 줄의 # 뒤에 한 칸을 띄고 작성한다.
__version__ = '0.1'  # 인라인 주석은 구문과 적어도 2칸 이상의 공백을 준다.
__author__ = 'whoever'  # 명백한 상황에서는 주석을 사용하지 않는다.

# import this
# import os,sys
# import os
# import sys

# import third_party_library
# from third_party_library import third_party_function

# import user_defined_library_1
# from pep8 import WutEver
# 모듈 명은 short_lower_case
# 패키지 명은 shortlowercase

class WutEver:
    """클래스명은 CamelCase로 작성하자.
    Docstring은 public 모듈, 함수, 클래스, 메소드에 대해 작성한다.
    선언문 바로 아래줄에 붙여서 작성한다.
    쌍따옴표 뒤에 바로 붙여서 작성을 시작한다.
    마지막 줄은 쌍따옴표 세 개로 마무리한다.
    한 줄짜리 Docstring은 같은 줄에 모든 내용을 넣어서 마무리한다.(_own 참고)
    """
    def __init__(self):
        """클래스의 생성자
        클래스의 인스턴스 메서드의 첫 번째 파라미터는 해당 객체를 가리킨다.
        이 파라미터는 변수명을 self로 지정하자.
        """
        print('class WutEver is created')

    def __repr__(self):
        """a = WutEver()
        print a 
        이 때 출력될 값을 정의할 수 있다.
        클래스 내부에서 정의하는 메서드는 줄 하나로 구분하자.
        """
        return ', '.join(dir(self))

    def _own(self):
        """클래스 속성 앞에 _를 붙이면 해당 속성을 해당 로컬에서만 사용한다는 의미이다(protected)"""
        pass

    def __func(self):
        """ 클래스 속성 앞에 __를 붙이면 해당 속성 앞에 '_class명'이 붙는다
        _WutEver__func
        (private)
        """
        pass


def so_wut(arg='', *args, **kwargs):
    """함수명은 lower_case 로 작성하자
    최상위 클래스와 메서드는 줄 2개로 구분하자.
    """
    pass


def keyword_arg(a, b=0):
    """키워드 인자나 디폴트 인자의 대입 연산은 공백을 넣지 않는다"""
    return so_wut(arg=a, kwarg=b)

# 변수 할당 앞뒤에는 스페이스를 하나만 사용하자
we = WutEver()
print we

tmp_list = [1, 2, 3, 4, 5]

# good / bad
so_wut(0, tmp_list[1], {'name': 'lee'})
so_wut(0, tmp_list[ 1 ], { 'name': 'lee' })

var_good_1 = 1
var_good_two = 2
var_good_three = 3

var_bad_1       = 1
var_bad_two     = 2
var_bad_three   = 3

# boolean
empty_list = []  # if empty_list (False)

# 혼동을 피하기 위해 l, O, I 등을 한 글자 변수로 사용하지 말 것.

# 프로그램을 짜기 전에 클래스의 멤버들을 public으로 할지 non-public으로 할지 우선적으로 고민하자.
# 애매하다면, 우선 non-public으로 한다. (반대의 경우보다 추후 수정이 용이함)
```
