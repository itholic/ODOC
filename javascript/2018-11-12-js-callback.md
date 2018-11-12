---
title: "[javascript] 콜백(callback) 함수"
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

# callback

callback을 그대로 해석하면 '다시 부른다'는 의미이다.

javascript에서 callback은 함수를 다시 부르는 것이다.

무슨말일까?

callback을 이해하려면 우선 비동기방식을 이해해야한다.

다음 Node.js 예제를 보자.

```js
// callback.js
  1 var fs = require("fs");
  2
  3 var contents = fs.readFile("sample.txt", "utf8")
  4
  5 console.log("contents : ", contents)
  6
  7 for (var i=0; i < 10; i++) {
  8     console.log("keep doing something")
  9 }
```

우선 fs모듈을 사용해 "sample.txt"라는 파일을 읽는다.

읽은 내용을 contents라는 변수에 담고, 내용을 출력한다.

그 이후 10번의 이터레이션을 하며 "keep doing something" 문자열을 출력한다.

실행해보자.

```
$ node callback.js
contents :  undefined
keep doing something
keep doing something
keep doing something
keep doing something
keep doing something
keep doing something
keep doing something
keep doing something
keep doing something
keep doing something
```

잘 동작한 것 같지만 뭔가 이상하다.

"sample.txt" 파일의 내용이 출력될줄 알았는데 undefined가 출력되었다.

이는 javascript가 기본적으로 비동기로 작동하기때문에 발생하는 현상이다.

<br/>

3번째 줄에서 readFile을 실행하면 디스크에서 "sample.txt"라는 파일을 읽는 I/O작업이 실행된다.

그럼 javascript는 이 작업이 끝날때까지 기다렸다가 다음 줄을 실행하는 것이 아니라,

readFile 명령만 던져버리고 실제 파일 읽기가 끝나기 전에 바로 다음줄로 넘어가버리는 것이다.

<br/>

어머니께서 된장찌개를 끓이는 중에 나에게 콩나물 심부름을 시키고, 하던 일을 계속 하시는 것이다.

근데, 심부름을 보낸지 1초만에 콩나물이 있는지 없는지 확인하니까 당연히 undefined가 출력된 것이다.

<br/>

그럼 비동기로 실행하지 말고, 기다렸다가 실행하면 안될까?

다음과 같이 readFile 함수를 readFileSync 로 바꾸어보자.

```js
// callback.js
  1 var fs = require("fs");
  2
  3 var contents = fs.readFileSync("sample.txt", "utf8")
  4
  5 console.log("contents : ", contents)
  6
  7 for (var i=0; i < 10; i++) {
  8     console.log("keep doing something")
  9 }
```

3번째 줄의 readFile만 readFileSync로 바뀌었다.

readFileSync는 비동기가 아닌 동기 방식으로 동작한다.

<br/>

어머니께서 콩나물 심부름을 시키고, 

내가 콩나물을 사올때까지 가스불을 꺼놓은채로 가만히 기다리시다가, 

콩나물이 도착하면 다시 가스불을 켜서 계속 된장찌개를 끓이는 것이다.

이는 딱봐도 매우 비효율적이지만, 어쨌든 작업 재개시 콩나물이 반드시 있다는 것을 보장한다.

실행해보자.

```
$ node callback.js
contents :  i am sample

keep doing something
keep doing something
keep doing something
keep doing something
keep doing something
keep doing something
keep doing something
keep doing something
keep doing something
keep doing something
```

파일의 내용이 정상적으로 출력되었다.

하지만 이렇게 비효율적으로 일을 처리해야할까?

<br/>

만약 파일의 내용이 어마어마하게 길다면, 

언제 끝날지도 모르는 긴 시간을 기다렸다가 다음 작업을 수행해야 하는 것이다.

단순히 "keep doing something" 이라는 문자열을 출력하는, 

파일의 내용과 전혀 상관 없는 작업들임에도 불구하고 말이다.

<br/>

그럼 첫 번째 방식처럼 비동기로 처리하되, 

파일의 읽기 작업이 끝나면 다시 알려주고,

그 때가 되면 파일의 내용을 출력해도 되지 않을까?

<br/>

어머니는 나에게 콩나물 심부름을 시키고 계속 된장찌개를 끓이시되,

내가 "엄마 콩나물 사왔어요" 라고 말하기 전까지는 콩나물을 찾지 않고, 다른 일에 집중하시는 것이다.

이 때, "엄마 콩나물 사왔어요" 라고 엄마를 '다시 부르는' 행위를 callback이라고 한다.

다음과 같이 코드를 바꿔보자.

```js
// callback.js
  1 var fs = require("fs");
  2
  3 fs.readFile("sample.txt", "utf8", function (err, contents) {
  4     console.log(contents)
  5 })
  6
  7 for (var i=0; i < 10; i++) {
  8     console.log("keep doing something")
  9 }
```

readFile의 마지막 인자로 `function (err, contents) { console.log(contents) }` 라는 익명 함수를 넘겨주었다.

이 익명 함수를 readFile의 callback 함수라고 칭하며,

readFile의 읽기 작업이 모두 끝난 이후에 실행된다.

실행해보자.

```
$ node callback.js
keep doing something
keep doing something
keep doing something
keep doing something
keep doing something
keep doing something
keep doing something
keep doing something
keep doing something
keep doing something
i am sample

```

코드 순서상으로는 4번쨰 줄의 "sample.txt"내용을 출력하는 부분이 우선임에도 불구하고,

8번쨰 줄의 "keep doing something"이 먼저 출력되었다.

그리고 마지막줄에 "sample.txt"의 내용 또한 undefined로 나오지 않고 제대로 출력되었다.

<br/>

이는 `function (err, contents) { console.log(contents) }` 라는 함수를 readFile 함수가 끝난 이후에 실행시켰다는 뜻이 된다.

이렇게 함으로써 비동기 환경에서도 내가 필요한 부분은 동기적으로 동작할 수 있도록 제어할 수 있다.

readFile이 먼저 실행되고 callback함수가 그 이후에 실행된 것처럼 말이다.

javascript는 싱글 스레드이며, 기본적으로 모든 함수가 비동기로 실행되기때문에 이는 아주 중요한 개념이다.

<br/>

참고로 함수를 또 다른 함수의 인자로 넘겨 실행할 수 있는 이유는 javascript에서 함수를 <a href="https://itholic.github.io/etc-first-class-citizen/" target="_blank">일급객체</a>로 취급하기 때문이다.

