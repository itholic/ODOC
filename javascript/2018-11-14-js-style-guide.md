---
title: "[javascript] 코딩 스타일 가이드(코딩 컨벤션)"
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

# javascript coding convention (style guide)

일반적인 프로그래밍 언어가 그러하듯, javascript에도 권장하는 코딩 규칙(스타일)이 있다.

여러 권장 방식중 <a href="https://google.github.io/styleguide/jsguide.html" target="_blank">구글에서 권장하는 방식</a>이 있는데, 

구글이 쓴다고해서 꼭 절대적인 규칙은 아니므로 참고정도로 보면 좋을 것 같다.

참고로 기존 프로젝트에서 사용하던 규칙이 있다면, 무조건 이 규칙보다 우선이다.


<br/>

변수와 함수명은 camelCase (단, 상수는 UPPER\_CASE)

```js
// good
let myName = 'itholic';

function printMyName(name) {
    console.log(myName);
};

// bad
let my_name = 'itholic';

function print_my_name(name) {
    console.log(my_name);
};
```

<br/>

상수(const)는 UPPER\_CASE로 명확히 표현

```js
// good
const NAME = "itholic";

// bad
const name = "itholic";
```

<br/>

변수 선언시 var대신 let이나 const를 사용 (이는 <a href="https://itholic.github.io/js-hoisting/" target="_blank">hoisting 관련 포스팅</a> 및 <a href="https://itholic.github.io/js-var-let-const/" target="_blank">변수 관련 포스팅</a> 참조)

```js
// good
let a = 1;

// bad
var a = 1;
```



<br/>


한 번에 하나의 변수만 선언

```js
// bad
let a = 1,
    b = 2,
    c = 3;

// good
let a = 1;
let b = 2;
let c = 3;
```


<br/>

파일명은 lower\_case 혹은 lower-case로 작성 (혼재해서 사용하지 말것)

```
// good
coding-convension.js
coding_style_guide.js

// bad
codingConvension.js
coding_style-guide.js
```


<br/>

들여쓰기는 탭이나 4칸공백보다는 2칸 공백을 권유

```js
// good
function foo() {
  var a
}

// bad
function foo() {
    var a
}
```


<br/>

문장의 끝에 세미콜론 기재를 권유 (자바스크립트는 세미콜론이 강요되지 않음)

```js
var a1 = 10;

functions foo() {
    var a2 = 20;
};
```


<br/>

Arrow Function으로 표현할 수 있는 부분은 가급적 Arrow Function으로 표현할 것

```js
// good
[1, 2, 3, 4, 5].map((x) => x * x);

//bad
[1, 2, 3, 4, 5].map(function(x) {
    return x * x; 
});
```


<br/>

문자열 연결시 + 보다는 탬플릿 문자열로 표현 (따옴표 모양 유심히 볼 것)

```js
let name = "itholic";

// good
console.log(`My name is ${name}`);

// bad
console.log("My name is " + name);
```


<br/>


문자열은 큰따옴표(") 보다는 작은따옴표(')를 사용, 문자열에 작은따옴표 포함시 탬플릿 문자열 사용 (`)

```js
// bad
let introduce = "i am itholic"

// good
let introduce = 'i am itholic' 

// good
let introduce = `i'm itholic`
```
