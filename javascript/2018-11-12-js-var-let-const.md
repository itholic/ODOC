---
title: "[javascript] var, const, let 차이"
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

# var, const, let

javascript에서 변수는 var, const, let 세 개의 키워드로 정의 가능하다.

우선 var와 const의 차이는 다음과 같다.

```js
// var.js
  1 var a = 10
  2 a = 11
```

위와 같이 var의 경우 변수를 할당하고 값을 바꿀 수 있다.

```js
// const.js
  1 const A = 10
  2 A = 11
```

하지만 const는 값을 바꾸려고 하면 다음과 같은 에러가 발생한다.

```
A = 11
  ^

TypeError: Assignment to constant variable.
    at Object.<anonymous> (/home/iris/nodetest/var.js:2:3)
    at Module._compile (internal/modules/cjs/loader.js:688:30)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:699:10)
    at Module.load (internal/modules/cjs/loader.js:598:32)
    at tryModuleLoad (internal/modules/cjs/loader.js:537:12)
    at Function.Module._load (internal/modules/cjs/loader.js:529:3)
    at Function.Module.runMain (internal/modules/cjs/loader.js:741:12)
    at startup (internal/bootstrap/node.js:285:19)
    at bootstrapNodeJSCore (internal/bootstrap/node.js:739:3)
```

이미 이름만 보고 짐작했을 수도 있지만, const는 상수이다.

그래서 한 번 지정한 값을 바꾸려고 하면 에러가 나는 것이다.

그럼 let은 어떨까?

```js
// let.js
  1 let a = 10
  2 a = 10
```

위 코드를 실행하면 var와 같이 에러가 나지 않는다.

그럼 일단 값을 변경할 수 있다는 점에서 const와의 차이는 명확히 알 것 같다.

그렇다면 let과 var의 차이는 무엇일까?

```js
// var_hoisting.js
  1 console.log(a)
  2 var a = 10
```

위 코드를 실행하면 `undefined`가 출력된다.

이는 변수 <a href="https://itholic.github.io/js-hoisting/" target="_blank">호이스팅</a>에 의해 var a 의 선언부가 위쪽으로 끌어 당겨져 발생하는 현상이다.

그럼 let은 어떨까?

```js
// let_hoisting.js
  1 console.log(a)
  2 var a = 10
```

위 코드를 실행하면 다음과 같은 에러가 발생한다.

```
/home/iris/nodetest/var.js:1
(function (exports, require, module, __filename, __dirname) { console.log(a)
                                                                          ^

ReferenceError: a is not defined
    at Object.<anonymous> (/home/iris/nodetest/var.js:1:75)
    at Module._compile (internal/modules/cjs/loader.js:688:30)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:699:10)
    at Module.load (internal/modules/cjs/loader.js:598:32)
    at tryModuleLoad (internal/modules/cjs/loader.js:537:12)
    at Function.Module._load (internal/modules/cjs/loader.js:529:3)
    at Function.Module.runMain (internal/modules/cjs/loader.js:741:12)
    at startup (internal/bootstrap/node.js:285:19)
    at bootstrapNodeJSCore (internal/bootstrap/node.js:739:3)
```

a가 아직 선언되지 않았다는 에러이다.

즉, 변수 호이스팅이 발생하지 않았다.

그럼 const의 경우는 어떨까?

```js
// const_hoisting.js
  1 console.log(a)
  2 const a = 10
```

위 코드를 실행하면 let의 경우와 완전히 동일한 에러가 출력된다.

마지막으로 간단히 var, const, let의 차이를 정리하자면 다음과 같다.

```
var   : 값의 변경 가능, 호이스팅 가능
let   : 값의 변경 가능, 호이스팅 불가
const : 값의 변경 불가, 호이스팅 불가
```

