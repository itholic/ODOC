# json

파이썬에서는 json파일을 손쉽게 다루기 위한 모듈을 제공한다.

json은 JavaScript Object Notation의 약자로, 

말그대로 자바스크립트에서 사용하는 객체 표현 방식이다.

근데 이 표현 방식이 꽤 효율적이라서 여기저기 많이 사용되고,

이러한 객체를 파일에 적어놓으면 그것을 json 파일이라고 한다.

json은 다음과 같이 표현한다.

```json
{
    "name": "itholic",
    "job" : "programmer",
    "age" : 29
}
```

python의 딕셔너리 타입과 매우 매우 매우 비슷하지 않은가?

그래서 파이썬에서는 json파일을 읽어서 이를 딕셔너리 타입으로 손쉽게 변환시킬 수 있다.

그리고 반대로 딕셔너리 타입을 json포맷으로 출력하는 것도 가능하다.

이러한 모든 과정은 json모듈이라는 녀석이 알아서 해준다.

위 json 예시를 json_sample이라는 파일로 저장하고, 파이썬에서 불러와보자.(디코딩)

```python
#-*- coding:utf-8 -*-

import json

with open('json_sample') as f:
    data = json.load(f)

print (type(data))  # <class 'dict'>
print (data)  # {'name': 'itholic', 'job': 'programmer', 'age': 29}
```

놀랄정도로 간단하다.

일반 파일과 똑같이 읽어서 json.load() 메소드를 사용하기만 하면 된다. 

출력 결과를 보면 알 수 있듯이 딕셔너리로 바로 사용 가능하다.

이번엔 딕셔너리를 json으로 변경해보자. (인코딩)

```python
#-*- coding:utf-8 -*-

import json

dict_sample = {'name': 'itholic', 'job': 'programmer', 'age': 29}

data = json.dumps(dict_sample)

print (type(data))  # <class 'str'>
print (data)  # {"name": "itholic", "job": "programmer", "age": 29}
```

마찬가지로 json.dumps 메소드를 사용해 매우 간단하게 작업을 완료했다.

출력을 좀 더 깔끔하게 하려면 다음과 같이 dumps 메소드에 indent 옵션을 주면 된다.


```python
#-*- coding:utf-8 -*-

import json

dict_sample = {'name': 'itholic', 'job': 'programmer', 'age': 29}

data = json.dumps(dict_sample, indent=2)

print (type(data))  # <class 'str'>
print (data)  
"""
{
  "name": "itholic",
  "job": "programmer",
  "age": 29
}
"""
```

indent옵션은 말 그대로 요소를 한 줄씩 출력하고, 들여쓰기(indent)를 몇 칸으로 할 것인지 지정하는 옵션이다.

