# logging_file

로깅은 파일, 스트림 방식이 있다.

파일 방식으로 로그를 남겨보자.


```python
# -*- coding:utf-8 -*-

"""logging 모듈 사용해 로그를 파일로 남겨보자"""

import logging

# 로거 생성 / 로깅 레벨 설정
logger = logging.getLogger("justlog")
logger.setLevel(logging.DEBUG)

# 파일 핸들러 생성
file_handler = logging.FileHandler("./logs/just.log")
# 만약, 파일 최대 사이즈와 최대 갯수를 지정하고 싶다면 다음과 같이 하면 된다.
# 5MB 크기의 파일을 최대 10개만 만들겠다.
# file_max_bytes = 5 * 1024 * 1024
# file_handler = logging.handlers.RotatingFileHandler("./logs/just.log"), maxBytes=file_max_bytes, backupCount=10)

# 로그 메시지 포맷 설정 (https://docs.python.org/3/library/logging.html#logrecord-attributes)
formatter = logging.Formatter("[%(levelname)s] '%(filename)s' %(asctime)s : %(message)s")
file_handler.setFormatter(formatter)

# 로거에 파일 핸들러 추가
logger.addHandler(file_handler)

# 로깅
logger.debug("for debug")
logger.info("for info")
logger.warning("for warn")

# 로거를 만들고, 핸들러를 만들고, 포매터 만든다.
# 역순으로 붙인다 (포매터를 핸들러에 붙이고, 핸들러를 로거에 붙임)
```
