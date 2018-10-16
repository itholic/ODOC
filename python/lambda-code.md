# lambda - code

lambda는 익명함수 혹은 일회성 함수이다.

여러번 재사용되는것이 아닌 일회성으로 사용되고 버려지는 함수를 짤때 유용하다.

말이 길어져봤자 이해에 도움이 안되므로, 일반 함수와 람다의 차이를 코드로 보자.

```python
# -*- coding:utf-8 -*-

"""lambda를 사용해 origin의 모든 값을 제곱한 새로운 리스트를 만들자"""

origin = [1, 2, 3, 4, 5]

# 1. 일반 함수 사용 예제
def func(x):
    square_x = x*x
    return square_x

squared = map(func, origin)  # OR squared = [func(item) for item in origin]
print("square all items using function : {}".format(squared))

# 2. 람다 사용 예제
squared = map(lambda x : x*x, origin)
print("square all items using lambda : {}".format(squared)) 

# map(함수명, 리스트) >> 리스트의 각 인자에 함수를 적용시킨 결과를 리스트로 반환
print(map(func, origin))

# lambda를 변수에 할당도 가능
f = lambda x : x*x
f(4)  # 16
f(5)  # 25
print(map(f, origin))  # [1, 4, 9, 16, 25]
```
