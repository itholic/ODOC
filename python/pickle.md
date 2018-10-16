# pickle

일반적으로 파일에 데이터를 쓸 때에는 문자열(string) 형식으로 쓴다.

하지만 가끔 list나 dict자료형 자체를 파일에 쓰고싶을때가 있다.

이런 상황을 위해 파이썬에서는 pickle 모듈을 지원한다.


```python
# -*- coding:utf-8 -*-

import pickle

fruit_store = {'apple':1000, 'banana':2000, 'tomato':'soldout', 'melon':'5000'}

## 에러 : write() argument must be str, not dict
#with open('./data/fruit.txt','w') as f:
#    f.write(fruit_store)

# pickle로 데이터를 다룰떄에는 byte방식으로 다루므로 'wb', 'rb'를 명시
# pickle로 파일 쓰기
with open('./data/fruit.txt','wb') as f:
    pickle.dump(fruit_store,f)

# pickle로 쓰인 파일 읽기
with open('./data/fruit.txt','rb') as f:
    data = pickle.load(f)
    print(data)  # {'apple':1000, 'banana':2000, 'tomato':'soldout', 'melon':'5000'}
```

데이터가 저장된 fruit.txt는 다음과 같이 바이너리 형태로 dict 데이터가 기록되어있다.

```
<80>^C}q^@(X^E^@^@^@appleq^AMè^CX^F^@^@^@bananaq^BMÐ^GX^F^@^@^@tomatoq^CX^G^@^@^@soldoutq^DX^E^@^@^@melonq^EX^D^@^@^@5000q^Fu.
```
