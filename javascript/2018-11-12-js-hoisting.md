---
title: "[javascript] 호이스팅(hoisting)"
layout: post
tag:
- javascript
- nodejs
category: javascript
author: itholic
sitemap:
  changefreq: daily
  priority: 1.0
---

# hoisting

hoising을 그대로 번역하면 '끌어 올리다' 라는 의미이다.

javascript에서는 변수를 끌어 올린다는 의미로 사용된다.

무슨 말일까?

```js
// hoisting.js
  1 console.log(name)
  2 var name = "itholic"
```

위 함수를 실행하면 에러가 나야할 것 같다.

name이라는 변수를 선언하기 전에 사용했기 때문이다.

하지만 실행하면 다음과 같은 결과가 나온다.

```
$ node hoisting.js
undefined
```

실제로 선언한 "itholic"이라는 값이 나오진 않았지만, 에러가 나지도 않았다.

파이썬에서 똑같은 예제를 실행해보자.

```python
# hoisting.py
  1 print(name)
  2 name = "itholic"
```

위 코드를 실행하면 다음과 같은 에러가 발생한다.

```
$ python hoisting.py
Traceback (most recent call last):
  File "hoisting.py", line 1, in <module>
    print(name)
NameError: name 'name' is not defined
```

그렇다면 javascript에서는 왜 에러가 발생하지 않을까?

바로 호이스팅 때문이다.

javascript에서는 위 코드를 내부적으로 다음과 같이 해석한다.

```js
// hoisting.js
  1 var name
  2 console.log(name)
  3 name = "itholic"
```

`var name = "itholic"` 의 선언부만 따로 떼어서 말그대로  '끌어 올렸다'.

그래서 console.log 부분에서 참조 에러가 나지 않고 undefined를 출력한 것이다.

이는 변수뿐 아니라 함수에도 똑같이 적용된다.

다음 예제를 보자.

```js
// hoisting_func.js
  1 printName();
  2
  3 function printName() {
  4     var name = "itholic"
  5     console.log("name : ", name)
  6 }
```

함수의 선언은 3번 라인에서 했지만, 1번 라인에서 바로 함수를 호출하고있다.

실행하면 다음과 같이 정상 실행된다.

```
$ node hoisting_func.js
name :  itholic
```

단, 다음과 같이 함수 표현식으로 익명함수를 변수에 할당한 경우는 호이스팅 되지 않는다.

```js
// hoisting_expression.js
  1 printName();
  2
  3 var printName = function() {
  4     var name = "itholic"
  5     console.log("name : ", name)
  6 }
```

위 코드를 실행하면 다음과 같은 에러가 발생한다.

```
$ node hoisting_expression.js
/home/iris/nodetest/hoisting_func.js:1
(function (exports, require, module, __filename, __dirname) { printName();
                                                              ^

TypeError: printName is not a function
    at Object.<anonymous> (/home/iris/nodetest/hoisting_func.js:1:63)
    at Module._compile (internal/modules/cjs/loader.js:688:30)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:699:10)
    at Module.load (internal/modules/cjs/loader.js:598:32)
    at tryModuleLoad (internal/modules/cjs/loader.js:537:12)
    at Function.Module._load (internal/modules/cjs/loader.js:529:3)
    at Function.Module.runMain (internal/modules/cjs/loader.js:741:12)
    at startup (internal/bootstrap/node.js:285:19)
    at bootstrapNodeJSCore (internal/bootstrap/node.js:739:3)
```

printName이 함수가 아니라는 에러가 발생했다.

이는 새로운것이 아니라, 앞서 설명했던 변수 호이스팅처럼 printName에 undefined가 선언된 것이다.

javascript가 내부적으로 다음과 같이 해석했다고 보면 된다.

```js
  1 var printName  // 아직 값이 할당되지 않았으므로 undefined
  2 printName();  // undefined를 함수처럼 사용하려고 했으므로 에러
  3
  4 printName = function() {
  5     var name = "itholic"
  6     console.log("name : ", name)
  7 }
```

함수 표현식은 결국 함수를 선언에 변수에 할당하는 것이므로, 변수 표현식과 똑같은 매커니즘으로 작동한다.

참고로 이렇게 함수를 변수에 할당할 수 있는건, javascript에서 함수를 <a href="https://itholic.github.io/etc-first-class-citizen/" target="_blank">일급객체</a>로 취급하기 때문이다.
