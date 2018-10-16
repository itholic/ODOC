# logging_stream

로깅은 파일, 스트림 방식이 있다.

스트림 방식으로 로그를 남겨보자.


```python
# -*- coding:utf-8 -*-

"""logging 모듈 사용해 로그를 스트림에 남겨보자"""

import logging

# 로거 생성 / 로깅 레벨 설정
logger = logging.getLogger("justlog")
logger.setLevel(logging.DEBUG)

# 파일 핸들러 생성
stream_handler = logging.StreamHandler()

# 로그 메시지 포맷 설정 (https://docs.python.org/3/library/logging.html#logrecord-attributes)
formatter = logging.Formatter("[%(levelname)s] '%(filename)s' %(asctime)s : %(message)s")
stream_handler.setFormatter(formatter)

# 로거에 파일 핸들러 추가
logger.addHandler(stream_handler)

# 로깅
logger.debug("for debug")
logger.info("for info")
logger.warning("for warn")
```
