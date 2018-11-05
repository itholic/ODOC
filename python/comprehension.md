# comprehension

comprehension은 일반적으로 '이해', '포함'이라는 뜻으로 사용하곤 하지만,

파이썬에서는 '함축'이라는 의미로 사용한다.

<br/>

그럼 뭐가 대체 함축이냐?

list, dict, set같은 <a href="https://itholic.github.io/python-iterable-iterator/" target="_blank">iterable</a>한 객체들을 만들때,

좀 더 함축적으로, 간결하게 표현할 수 있다는 의미이다.

<br/>

그럼, expression은 무엇이냐?

이는 사실상 comprehension과 완전 동일한 개념을 <a href="https://itholic.github.io/python-generator/" target="_blank">generator</a>에 적용한 것 뿐이므로,

comprehension을 설명하는 중간에 잠깐 언급하도록 하겠다.

바로 예제를 보자.

### 예제

다음과 같이 다섯 개의 숫자를 담고있는 sample_list라는 녀석이 있다.

```python
sample_list = [1, 2, 3, 4, 5]

```

이 리스트의 모든 요소에 2를 곱한 새로운 리스트를 생성하고 싶다.

[2, 4 ,6, 8, 10] 이라는 리스트를 만들고 싶다는 뜻이다.

일반적으로는 이렇게 한다.

```python
doubled_list = []
for item in sample_list:
    doubled_list.append(item*2)
```

빈 리스트를 선언하고,

기존 sample_list를 iteration하며(for문을 돌며),

요소에 2씩 곱해서 append 해주었다.

comprehension을 사용하면 다음과 같이 함축적으로 표현 가능하다

```python
doubled_list = [item*2 for item in sample_list]
```

처음 봤을땐 "이게 뭐지?" 하겠지만,

하나하나 기존의 코드과 비교해보면 대충 어떤 규칙을 가지고있는지 감이 올것이다.

for문을 돌며 하고자 하는 동작(item*2)을 먼저 기술하고, 그 뒤에 for문이 바로 따라온다.

for문 다음에 개행과 indentation을 따로 신경쓸 필요도 없어서 한 줄에 깔끔하게 표현이 가능하다.

또한 빈 리스트를 미리 선언해줄 필요도 없이, 선언과 동시에 값을 할당 가능하다.

그리고 마지막으로 대괄호 '[ ]'로 묶어주었다.

<br/>

대괄호가 아닌 중괄호 '{ }'로 묶어주면 list가 아닌 set을 반환한다.

```python
doubled_set = {item*2 for item in sample_list}
print(type(doubled_set))  # <type 'set'>
```

<br/>

대괄호가 아닌 소괄호 '( )'로 묶어주면 list가 아닌 generator를 반환한다.

```python
doubled_gen = (item*2 for item in sample_list)
print(type(doubled_gen))  # <type 'generator'>
```

그리고 이러한 방식을 generator comprehension이라고 부르지 않고,

generator expression이라고 칭하는 것 뿐이다.

따라서 'expression과 comprehension이 무슨 차이일까?' 에 관해 그렇게 깊게 생각하지 않아도 된다.

다만, generator로 생성했을때는 값 호출시 <a href="https://itholic.github.io/python-lazy-evaluation/" target="_blank">Lazy Evaluation</a>으로 동작하기 때문에 이 부분을 유의하면 된다.

<br/>

참고로, 같은 코드를 lambda를 활용해 작성할 수 있다.

```python
doubled_list = list(map((lambda item:item*item), sample_list))
```

개인적으로 list comprehension으로 표현한 것이 훨씬 가독성이 좋다고 생각하지만,

이는 개개인의 취향이므로 더 언급하지는 않겠다.

<br/>

마지막으로, dict comprehension을 사용해보자.

다음과 같이 key 값만 저장한 리스트와 value값만 저장한 리스트가 있다고 하자.

```python
k_list = ["name", "age", "gender"]
v_list = ["itholic", 29, "male"]
```

이를 사용해 dict를 만든다면, 일반적으로는 다음과 같이 만들것이다.

```python
my_dict = {}
for k, v in zip(k_list, v_list):
    my_dict[k] = v
```

이를 dict comprehension으로 표현하면 다음과 같다.

```python
my_dict = {k:v for k, v in zip(k_list, v_list)}
```


참고로 zip 명령어는 두 개의 리스트를 인자로 받아서, 양쪽 리스트의 동일한 인덱스 요소를 짝지어주는 역할을 한다.

예제를 보자.

```python
k_list = ["name", "age", "gender"]
v_list = ["itholic", 29, "male"]

zip(k_list, v_list)  # [('name', 'itholic'), ('age', 29), ('gender', 'male')]
```

### 결론

성능적인 측면에서는 일반인 for문을 쓰나, comprehension을 쓰나 차이는 없다.

그리고 comprehension 방식에 익숙하지 않은 사람은 기존 방식이 훨씬 편하다고 할 수도 있다.

나 또한 comprehension에 익숙해지기 전까지는 굳이 써야할 필요성을 느끼지 못했다.

<br/>

하지만 어느정도 익숙해지고 난 이후,

기존에 작성했던 코드를 리팩토링 하며 일반 for문을 comprehension으로 바꾸어보았더니,

전체적으로 코드가 훨씬 깔끔해지고 가독성이 높아진 것을 체감했다.

<br/>

그렇다고해도 이는 어디까지나 주관적인 경험이며, 결국 본인이 편하다고 생각하는 것을 사용하면 된다.

실제로 for문에서 해야하는 연산이 복잡할 경우,

굳이 comprehension을 사용해 한 줄에 우겨넣으려다가 오히려 가독성을 해칠수도 있다.

<br/>


다만, '알고 사용하지 않는 것'과 '몰라서 사용하지 못하는 것'은 완전히 다르기때문에,

다른 사람의 코드를 읽을 경우를 대비해서라도 이런 방식에 대해 어느정도 감은 잡아두는 것이 좋다.
