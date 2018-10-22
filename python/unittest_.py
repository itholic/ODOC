#-*- coding: utf-8 -*-
"""
파이썬에서는 단위테스트를 위한 unittest라는 유용한 자체 모듈을 제공한다
"""

import unittest
import os
import FileHandler


class FileHandlerTest(unittest.TestCase):
    testfile = "./data/test"

    # setUp : 유닛테스트 시작하기 전에 실행되는 함수
    def setUp(self):
        with open(self.testfile, "w") as f:
            f.write('1\n2\n3\n4\n5\n6')

    # tearDown : 유닛테스트 종료 후 실행되는 함수
    def tearDown(self):
        try:
            os.remove(self.testfile)
        except:
            pass

    # 테스트 함수
    def test_file_line_counter(self):
        self.assertEqual(FileHandler.file_line_counter(self.testfile), 5)

if __name__ == "__main__":
    unittest.main()