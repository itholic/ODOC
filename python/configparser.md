# configparser

소프트웨어 동작에 필요한 특정 설정 값들은 보통 코드에 직접 넣지 않는다.

이는 보안 및 유지보수와 관련된 이슈이며, 따라서 보통 .conf등의 설정 파일에서 읽어오는 식으로 동작한다.

파이썬에서는 이를 쉽게 사용할 수 있도록 도와주는 configparser라는 모듈이 있다.

```python
"""conf 파일 내용
[USER]
id = itholic
passwd = 123
email = itholic@it.com

[SYS]
ip = 127.0.0.1
port = 8000
"""

# -*- coding:utf-8 -*-

import configparser

path = './conf/test.conf'  # path도 이렇게 하드코딩하지 않고, 사용자 입력으로 받는경우가 많다

config = configparser.ConfigParser()  # ConfigParser 객체 생성
config.read(path)  # conf 파일 읽어옴

user_id = config.get('USER', 'id')  # itholic
sys_ip = config.get('SYS', 'ip')  # 127.0.0.1
```
