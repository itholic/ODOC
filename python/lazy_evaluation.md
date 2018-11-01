# Lazy Evaluation 

만약 당신이 스터디룸에서 일하는 직원이다.

이 스터디룸은 스터디 공간뿐 아니라, 간단한 간식도 제공한다.

오후 7시에 10명이 스터디룸을 예약하고, 간식으로 컵라면을 주문해놓았다.

하지만 예약한 손님이 말하길, 

"다들 바빠서 최악의 경우 한두명밖에 참석하지 못할수도 있어요."

당신이 직원이라면 컵라면 10개를 미리 다 끓여 놓겠는가?

아니면 언제든 최대 10명까지 제공할 수 있는 상태로 준비만 해 두겠는가?

확실히 10명이 제시간에 온다는 보장이 있다면 전부 미리 물을 부어놓은게 효율적이겠지만,

이 상황은 당연히 후자가 효율적이다.

후자의 경우가 바로 Lazy Evaluation이다.

<br/>

Lazy Evaluation은 어떤 값이 실제로 쓰일 때 까지 그 값의 계산을 뒤로 미루는 동작 방식이다.

이는 <a href="https://itholic.github.io/python-generator/" target="_blank">Generator</a>에 대한 이해가 선행되어야 이해하기 수월하지만, 딱히 몰라도 된다.

다음과 같이 숫자 1을 반환하는 단순한 함수가 있다.

반환하기 전에 "return 1" 이라는 문자열을 출력한다.

```python
def return_one():
    print("return 1")
    return 1 
```

그리고 다음과 같이 return_one을 10번 수행해서,

숫자 1을 10개 담는 리스트를 만들어보자.

```python
def return_one():
    print("return 1")
    return 1

print("let's make one_list !")
one_list = [return_one() for x in range(10)]
```

마지막으로, 만든 리스트(one_list)에서 값을 하나씩 꺼내 출력해보자.

```python
def return_one():
    print("return 1")
    return 1

print("let's make one_list !")
one_list = [return_one() for x in range(10)]

print("let's print one_list !")
for one in one_list:
    print(one)
```

출력 결과는 다음과 같다.

```
let's make one_list !
return 1
return 1
return 1
return 1
return 1
return 1
return 1
return 1
return 1
return 1
let's print one_list !
1
1
1
1
1
1
1
1
1
1
```

특별할거 없다.

one_list를 출력하기 전에 미리 함수 10번이 실행되어 값을 다 만들어 리스트에 저장해놓았다.

그럼 앞선 예제의 one_list를 generator로 만들어보자.

list comprehension에서 대괄호만 소괄호로 바꾸어주면 generator expression이 된다.

즉, 다음과 같이 바꾸면 리스트 대신 제네레이터를 만들어준다는 뜻이다.

```python
def return_one():
    print("return 1")
    return 1

print("let's make one_list !")
one_list = (return_one() for x in range(10))  # 대괄호[] 를 소괄호() 로 바꿈

print("let's print one_list !")
for one in one_list:
    print(one)
```

실행해보자.

```
let's make one_list !
let's print one_list !
return 1
1
return 1
1
return 1
1
return 1
1
return 1
1
return 1
1
return 1
1
return 1
1
return 1
1
return 1
1
```

차이가 보이는가?

list의 값을 출력했을 때에는, 실제로 해당 list를 출력을 하든 말든 우선 값을 다 만들어놓았었다.

앞선 예제에서 "return 1"이라는 출력이 "let's pring one_list" 이전에 이미 10번 수행된 것을 보면 알 수 있다.

하지만 generator의 값을 출력했을 때에는, 실제로 generator의 값을 출력하는 순간에 함수에서 값을 만들고있다.

즉, 값이 실제로 사용되지 않으면 연산 또한 하지 않고, 시간과 메모리를 절약할 수 있다.

<br/>

예제를 너무 간단한 것을 들어 체감이 안될수도 있으니 이렇게 생각해보자.

예를들어 시간이 5초 이상 걸리는 아주 복잡한 연산이 있는데,

해당 연산으로 도출한 결과물을 최대 5개까지 사용 할 수도 있고, 아예 사용하지 않을 수도 있다고 해보자.

(마치 스터디룸에 손님이 최대 10명까지 올 수도 있지만, 아무도 오지 않을 수도 있는 것 처럼)

사용하지 않으면 아예 연산을 할 필요가 없겠지만,

어쨌든 사용 할 수도 있으니 리스트를 만들긴 만들어놓아야한다.

(최소한 컵라면 10개와 끓일 물 정도는 준비가 되어야 하지 않겠는가?)

<br/>

어쨌든 5개의 값을 전부 연산해 25초라는 시간을 소요해 list로 만들어 놓았는데,

프로그램이 종료 될 때까지 해당 값이 한 번도 사용되지 않았다면?

이런 상황에서는 연산 결과의 목록을 list보다는 generator로 만들어놓는게 효율적이다.

무조건 25초를 소비하고 들어가는 list에 비해서,

프로그램이 종료 될 때까지 값이  2번 사용되었다면 10초.

한 번도 사용되지 않았다면 연산에 단 1초도 사용되지 않을 것이기 때문이다.

<br/>

이처럼 Lazy Evaluation을 적절히 활용하면,

라면을 미리 다 끓여놓았다가 아무도 오지 않아서 다 버려야하는 상황을 방지할 수 있다.

시간을 들여 연산하고 메모리까지 할당해 놓았는데, 

프로그램이 종료될때까지 사용되지 않으면 억울하니까 Lazy Evaluation을 적절히 활용하자.

