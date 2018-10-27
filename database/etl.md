
# ETL

일을 하다보면 심심치 않게 ETL이라는 단어가 많이 들린다.

(직종에따라 전혀 들을 일이 없을 수도 있겠지만)

가끔 테이블명도 ETL이라고 되어있거나, 접두어나 접미어로 붙어있는 경우가 있다.

ETL은 그냥 단어 자체를 풀이하자면 추출(Extract), 변환(Transform), 적재(Load) 인데,

아마 처음 들어보는 사람이 이런 복잡한(?) 용어를 통해 ETL을 제대로 이해하기는 쉽지 않을 것 같다.

그래서 나 또한 ETL이 무엇인지 감이 잘 안잡혀서 이참에 공부를 해보았는데, 생각보다 복잡한 개념은 아니었다.

역시 IT는 항상 용어와의 싸움인 것 같다.

## 시나리오

그냥 아주 단순하게 이런 상황을 생각해보자.

연월일시분초(yyyyMMddHHmmss)가 각각 한컬럼에 저장된 테이블이 있다.

![etl_1](./img/etl_1.png)


그리고 내가 어떤 분석프로그램을 돌리기 위해 이 테이블에 있는 숫자를 써야하는데,

그 분석 프로그램에는 이런 조건으로 테이블을 생성해달라고 하고 있다.

1. 연/월/일/시분 4개로 이루어진 컬럼
2. 시분은 4자리로 입력

즉, 다음과 같은 형태를 원하는 것이다.

![etl_2](./img/etl_2.png)

그럼, 이런 테이블을 만들기 위한 과정을 간단히 살펴볼까?

### 1. 기존 테이블의 데이터 추출(Extract)

추출이란 말을 너무 어렵게 생각하지 말자,

SQL의 SELECT를 통해 데이터를 가져오는 걸 생각하면 된다.

우리가 필요한 데이터는 연/월/일/시/분이다.

분석프로그램에서 '초'는 필요로하지 않기 때문이다.

파이썬을 예로 들어보겠다. (원본 테이블은 test.db의 origin_table이라는 이름이라고 가정하자)

```python
# -*- coding:utf-8 -*-

import sqlite3

conn = sqlite3.Connection("test.db")
c = conn.cursor()

# 연, 월, 일, 시분을 가져올 쿼리
sql = '''
    select 연, 월, 일, 시, 분
    from origin_table
'''

# 각 결과 값을 담을 리스트
year = []
month = []
day = []
hour = []
min = []

# 쿼리 실행
c.execute(sql)

# 쿼리 결과를 리스트에 추가
for row in c:
    year.append(row[0])
    month.append(row[1])
    day.append(row[2])
    hour.append(row[3])
    min.append(row[4])

# 잘 추가되었는지 확인
print year  # [2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018]
print month  # [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
print day  # [27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27]
print hour  # [9, 11, 14, 14, 15, 16, 17, 17, 17, 17, 18, 19, 19, 20]
print min  # [12, 55, 32, 14, 16, 52, 40, 14, 33, 1, 21, 26, 13, 7]


```

테이블에서 데이터를 잘 추출(Extract)해서 변수에 넣어두었다.

파이썬 코드에 익숙하지 않다면, 그냥 단순히 테이블에서 데이터를 꺼내왔다고 생각하면 된다.

이제 이 데이터를 분석을 위한 데이터로 변환해보자.

### 2. 추출한 데이터의 변환 (Transform)

분석프로그램에서는 시와 분을 한 컬럼에 넣어달라고 요구했다.

그리고 4자리로 표현해야한다고 했다.

예를들어 9시 3분은 '0903'와 같은 형태로 저장하면 된다.

```python
def num_list_to_double_digit(list):
    """ 2자리 이하의 숫자로 구성된 리스트를 받아서, 1자리일 경우 앞에 0을 붙여 반환 """
    # 숫자가 1자리일 경우 앞에 '0'을 붙이기 위해 string으로 변환
	list = [str(data) for data in list]

    for i, data in enumerate(list):
        list[i] = data if len(data) == 2 else '0' + data

    return list

hour = num_list_to_double_digit(hour)
min = num_list_to_double_digit(min)

print hour  # ['09', '11', '14', '14', '15', '16', '17', '17', '17', '17', '18', '19', '19', '20']
print min  # ['12', '55', '32', '14', '16', '52', '40', '14', '33', '01', '21', '26', '13', '07']

```

hour과 min이 각각 2자리 형태로 잘 변환되었다.

마지막으로 hour과 min을 합쳐서 4자리로 만들자.

```python
hm = [hour[i] + min[i] for i in range(len(hour))]
print hm  # ['0912', '1155', '1432', '1414', '1516', '1652', '1740', '1714', '1733', '1710', '1821', '1926', '1913', '2007']
```

hour과 min의 각 요소를 합쳐서 hm 이라는 리스트를 만들었다.

이제 변환된 데이터를 새로운 테이블에 적재하기만 하면 된다.

참고로,

애초에 쿼리를 다음과 같이 던지면 굳이 이런 과정을 거치지 않아도 추출과 동시에 가공까지 한 번에 가능하다.

하지만 본 글에서는 ETL의 각 과정을 보다 상세히 알아보기 위해 굳이 귀찮은(?) 과정을 거쳤다.

```sql
select 연, 월, 일, substr('00'||시, -2, 2) || substr('00'||분, -2, 2) as '시분'
from origin_table
```


### 3. 추출 및 변환한 데이터의 적재(Load)


이제 변환이 끝났으니 적재(INSERT)해보자.

'연/월/일/시분' 네 개의 컬럼을 가지고있는 transformed_table 이라는 테이블을 만들고,

앞서 가공한 데이터를 넣어보자.

```python
# 테이블 생성 쿼리
sql_create_transformed_table = """
    create table transformed_table(연, 월, 일, 시분)
"""

# 데이터 삽입 쿼리
sql_insert_transformed_data = """
    insert into transformed_table values(?, ?, ?, ?)
"""

# 테이블 생성
c.execute(sql_create_transformed_table)

# 데이터 삽입
for i in range(len(year)):
    c.execute(sql_insert_transformed_data, (str(year[i]), str(month[i]), str(day[i]), hm[i]))

# 삽입 데이터 확인 (1개만 샘플로 확인)
c.execute("select * from transformed_data limit 1")
for row in c:
    print row[0], row[1], row[2], row[3]  # 2018 10 27 0912
```

제대로 적재(Load)가 된 것을 확인했다.

### 결론

허접하긴 하지만, 직접 ETL을 체험해봤다.

즉, ETL을 정말 간단하게 정의 해보자면 이렇다.

**"한 곳에 저장된 데이터를 필요에 의해 다른 곳으로 이동하는 것"**

본 예제처럼 기존 데이터의 형태와 컬럼 갯수를 조금 변형하여 재 적재하는 과정일수도 있지만,

굳이 데이터의 형태나 컬럼 갯수를 변형하지 않는 작업이 될수도 있다.

예를들어 sqlite3을 사용하다가 oracle로 데이터를 이전하고 싶을 경우,

데이터의 형태와 컬럼 갯수는 그대로 가져간 채, 단순히 테이블의 스키마를 조금 변형하는 작업이 될 수도 있다.

그리고 오픈소스나 상용으로 ETL을 제공하는 소프트웨어들은 이러한 일련의 과정을 조금 더 편하게 할 수 있도록 도와주는 역할을 하는 것 뿐이므로, ETL을 너무 복잡하게 생각하지 말자. (어떤 기술이든 실제로 적용하려면 복 하지만)