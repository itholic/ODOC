# sqlite3

python에는 sqlite3 모듈이 내장되어있어 손쉽게 db활용이 가능하다.


```python
# -*- coding:utf-8 -*-

import sqlite3
import os

db_path = "./test.db"
data = (1, 'itholic', 'seoul')
many_data = [
    (2, 'it', 'busan'),
    (3, 'holic', 'incheon'),
    (4, 'git', 'usa')
]
script = """
    create table t2(
        one,
        two,
        three
    );

    insert into t2 values(1, 'hi', 'bye');
"""

# db 존재하면 삭제
if os.path.exists(db_path):
    os.remove(db_path)

# conn 객체 생성
conn = sqlite3.Connection("test.db")

# cursor 객체 생성
c = conn.cursor()

# 쿼리
c.execute("create table t(a, b, c);")

c.execute("insert into t values(?, ?, ?)", data)
c.execute("insert into t values(:id_, :name, :location)", {"id_": "5", "name": "hub", "location": "norway"})
c.executemany("insert into t values(?, ?, ?)", many_data)
c.executescript(script)

c.execute("select * from t")
c.fetchone()  # (1, u'itholic', u'seoul')
c.fetchall()  # [(5, u'hub', u'norway'), (2, u'it', u'busan'), (3, u'holic', u'incheon'), (4, u'git', u'usa')]

conn.close()
```

with 절을 사용해 다음과 같이 사용도 가능하다. 

with절이 끝날때 자동으로 close() 해준다.

```
with sqlite3.Connection("test.db"):
    c = conn.cursor()
    
    c.execute("create table t(a, b, c);")
    
    c.execute("insert into t values(?, ?, ?)", data)
    c.execute("insert into t values(:id_, :name, :location)", {"id_": "5", "name": "hub", "location": "norway"})
    c.executemany("insert into t values(?, ?, ?)", many_data)
    c.executescript(script)
    
    c.execute("select * from t")
    c.fetchone()  # (1, u'itholic', u'seoul')
    c.fetchall()  # [(5, u'hub', u'norway'), (2, u'it', u'busan'), (3, u'holic', u'incheon'), (4, u'git', u'usa')]  
```
