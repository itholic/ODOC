# unittest

python에서는 unittest 모듈을 제공해, 손쉽게 단위 테스트를 할 수 있도록 지원한다

```python
# file_handler.py
#-*- coding: utf-8 -*-


# 테스트할 함수 : 파일 경로를 입력하면 해당 파일의 라인수를 반환
def file_line_counter(file_path):
    with open(file_path,"r") as f:
        lines = f.readlines()

    return sum(1 for line in lines)
```

위와 같은 함수를 테스트하고 싶다면, 다음과 같이 unittest 모듈을 활용해 테스트를 작성하면 된다

```python
#-*- coding: utf-8 -*-

import unittest
import os
import file_handler


class FileHandlerTest(unittest.TestCase):
    testfile = "./data/test"

    # setUp : 유닛테스트 시작하기 전에 실행되는 함수 (테스트 파일 생성)
    def setUp(self):
        with open(self.testfile, "w") as f:
            f.write('1\n2\n3\n4\n5\n6')

    # tearDown : 유닛테스트 종료 후 실행되는 함수 (테스트 파일 삭제)
    def tearDown(self):
        try:
            os.remove(self.testfile)
        except:
            pass

    # 테스트 함수 (arrsertEqual 메소드를 통해 기대하는 결과가 나오는지 테스트)
    def test_file_line_counter(self):
        self.assertEqual(file_handler.file_line_counter(self.testfile), 6)

if __name__ == "__main__":
    unittest.main()
```

성공하면 다음과 같은 문장이 출력된다.

```python
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

실패하면 다음과 같은 문장이 출력된다.

```python
======================================================================
FAIL: test_file_line_counter (__main__.FileHandlerTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:/git_store/ODOC/python/unittest_.py", line 28, in test_file_line_counter
    self.assertEqual(file_handler.file_line_counter(self.testfile), 5)
AssertionError: 6 != 5

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)

```

실패시 정확히 어떤 테스트 함수에서 실패했는지 알려주기 때문에, 손쉽게 디버깅이 가능하다

따라서, 테스트 함수는 일반 함수명 작성과는 달리 최대한 상세하게 기술하는 것이 유리하다.

테스트 함수명만 보고 어떤 함수가 실패했는지 손쉽게 알아보기 위함이다.