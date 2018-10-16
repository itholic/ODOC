# csv

csv(comma separated values)는 말그대로 각 라인의 컬럼이 콤마로 구분된 텍스트파일이다.

파이썬에서는 이를 읽어서 쉽게 사용할 수 있게 해주는 모듈을 제공한다.


```python
"""./data/test.csv 파일의 내용
1,2,3
4,5,6
7,8,9
"""

# -*- coding:utf-8 -*-

import csv

# csv 파일 읽기
with open('./data/test.csv','r') as f:
    data = csv.reader(f)  # csv.reader를 통해 데이터를 list in list
    print([line for line in data])  # [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

# csv 파일 쓰기
with open('./data/test.csv','a') as f:
    w = csv.writer(f)
    w.writerow([10, 11, 12])
    w.writerow([13, 14, 15])

# 쓴 내용 확인
with open('./data/test.csv','r') as f:
    data = csv.reader(f)  # csv.reader를 통해 데이터를 list in list
    print([line for line in data])  # [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['10', '11', '12'], ['13', '14', '15']]


```

separator가 콤마가 아닌 tab같은 다른 문자일 경우,
```python
csv.reader(f, delimiter='\t')
csv.writer(f, delimiter='\t')
```
이런식으로 delimiter를 지정해주면 된다.
