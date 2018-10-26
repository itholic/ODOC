# iterable? iterator?

파이썬뿐 아니라 일반적인 프로그래밍 언어에는 iterator라는 개념이 있다.

그리고 이 개념은 종종 iterable이라는 개념과 혼동된다.

나도 많이 헷갈려서 이참에 제대로 정리를 하려고 공부했는데,

이 두개의 개념을 자꾸 뭔가 상반되는 개념처럼 '차이'를 알아보려고해서 헷갈렸던 것 같다.

차이를 알아보려고 하지말고, 그냥 단어만 놓고 생각해보자.

iter'able'이라는 말은 무언가 '가능하다'라고 말하는 것 같지 않은가?

그렇다, **iterable한 객체라는건 단순히 iterator로 변환 가능한 객체를 의미한다.**

말로만 떠들지 말고 한 번 예제를 보자.

iterable 객체는 평소에 자주 사용하는 list나 dictionary등이 있다.

```python
li = [1, 2, 3, 4, 5]

print(li)  # [1, 2, 3, 4, 5]
print(li[1:4])  # [2, 3, 4]

next(li)  # 'list' object is not an iterator
```

우선 list를 print해서 한 번에 여러개의 값이 반환 가능한 것을 확인했다.

하지만 next 메소드를 써서 한 번에 한개씩 순차적으로 접근하려고 해보니,

list 객체가 iterator가 아니라는 에러가 발생한다.

그렇다면 list는 과연 iterable한 객체인가?

즉, list는 과연 iterator로 변환 가능한 객체인가?

다음과 같이 iter 메소드를 사용해보자.

```python
li = [1, 2, 3, 4, 5]

li_iter = iter(li)

next(li_iter)  # 1
next(li_iter)  # 2
next(li_iter)  # 3
next(li_iter)  # 4
next(li_iter)  # 5
next(li_iter)  # StopIteration
```

iter메소드를 사용하니 순차적인 접근이 가능해졌다.

li_iter의 타입을 확인해보자


```python
li = [1, 2, 3, 4, 5]

li_iter = iter(li)

type(iter)  # <class 'list_iterator'>
```

정말 list_iterator라는 iterator로 변환되었다.

**list는 iterator로 변환이 가능하므로, iterable한 객체이다.**

잠깐 for문을 생각해보자.

```python
li = [1, 2, 3, 4, 5]
for item in li:
    print(item)  # 1, 2, 3, 4, 5 순차 출력
```

for문에 list를 넣어 돌리면 순차적인 접근이 가능하다.

사용자가 명시적으로 list를 iterator로 바꾸어주지 않았음에도 불구하고 말이다.

이는 for문에서 내부적으로 list를 iterator로 바꾸어 순차접근을 하고있는것이다.

즉, for문을 돌려서 순차접근이 가능한 객체는 모두 iterable하다고 할 수 있다.

이런 관점에서 보면 string도 iterable한 객체이다.

```python
st = 'hello'

for c in st:
    print(c)  # h, e, l, l, o 순차 출력
```

이제 iterable과 iterator의 관계에대해 어느정도는 감이 잡혔으리라 생각한다.

두 개의 개념을 동일선상에 두고 비교하려고하면 헷갈린다.

하지만 예제를 통해 iterable한 객체는 iterator로 변환 가능하고,

for문 내에서 순차 접근이 가능한 객체라고 생각하면, 

두 개념의 '관계'에 대한 이해가 보다 순조로울 것이다.
