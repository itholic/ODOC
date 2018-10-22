#-*- coding: utf-8 -*-

import unittest
import os

# 테스트할 함수
def file_line_counter(file_path):
    with open(file_path,"r") as f:
        lines = f.readlines()

    return sum(1 for line in lines)