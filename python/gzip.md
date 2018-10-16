# gzip

파일이 압축되어있는 경우, 압축을 일일이 풀어서 내용을 읽는 것이 번거로울 수 있다.

파이썬에서는 압축된 파일의 내용을 바로 읽을 수 있게 해주는 모듈을 제공한다.

```python
# -*- coding:utf-8 -*-

import gzip

path = './data/test.csv.gz'

# 그냥 읽으면 바이너리값 그대로 출력
with open(path,'rb') as f:
    print(f.readlines())  # [b'\x1f\x8b\x08\x08\xdb\x85\xc5[\x00\x03test1.csv\x00\r\xc6\xb9\x11\x00 \x0c\x03\xc1\xdc3\xea\xe4\x02dl\x9e\xfe\x1b\x83\x8d\xd6$SQ4K\xb19\\\x85\x076\xce\xbf\x89\x0b\xb7\xe2\x01N,\x9a\x1c)\x00\x00\x00']


# gzip으로 읽으면 파일 원본 내용 출력
with gzip.open(path,'rb') as f:
    print(f.readlines())  # [b'1,2,3\r\n', b'4,5,6\r\n', b'7,8,9\r\n', b'10,11,12\r\n', b'13,14,15\r\n']


# 압축하기
path = './data/fruit.txt'
with open(path,'rb') as f_in:
    with gzip.open(path+'.gz','wb') as f_out:
        f_out.writelines(f_in)  # ./data/fruit.txt.gz 압축 파일 생성
```
