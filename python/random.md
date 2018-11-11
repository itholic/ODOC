
# random

코딩을 하다보면 랜덤 값을 만들고싶은 경우가 있다.

파이썬에서는 random모듈을 사용해 간단하게 랜덤 값을 생성할 수 있다.

```python
import random

# randrange
random.randrange(10)  # 0부터 9사이의 랜덤 int 생성
random.randrange(0, 10)  # 0부터 9사이의 랜덤 int 생성

# randint
random.randint(0, 10)  # 0부터 10사이의 랜덤 int 생성
# random.randint(10)  # 에러

# random
random.random()  # 0부터 1 사이의 랜덤 float 생성
# random.random(0, 1)  #  에러
# random.random(1)  # 에러

# uniform
random.uniform(0, 10)  # 0부터 10 사이의 랜덤 float 생성
# random.uniform(10)  # 에러
# random.uniform()  # 에러
```


그리고 랜덤 값을 생성하는 것 뿐만 아니라,

다음과 같이 list에서 임의의 값을 뽑아낸다거나 list의 순서를 섞는다거나 하는 것도 가능하다.


```python
import random

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list 값 섞기 (tuple, dict 에서는 불가능)
random.shuffle(num_list)
print(num_list)  # [2, 8, 9, 7, 10, 6, 4, 1, 3, 5]

# list, tuple 에서 임의의 값 뽑아내기 (dict에서는 불가능)
random.choice(num_list)  # 10
random.choice(num_list)  # 6
random.choice(num_list)  # 9
random.choice(num_list)  # 3
random.choice(num_list)  # 4
random.choice(num_list)  # 3


# list, tuple, dict 에서 임의의 값을 특정 갯수만큼 뽑아내기 (샘플링)
random.sample(num_list, 5)  # [2, 4, 1, 6, 7]
random.sample(num_list, 4)  # [8, 9, 7, 4]
random.sample(num_list, 3)  # [9, 8, 1]
random.sample(num_list, 2)  # [5, 6]
random.sample(num_list, 1)  # [7]
```
