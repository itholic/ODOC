# \==, ===, !=, !==

javascript에서는 \== 비교와 === 비교가 있다.

무슨 차이일까?

결론부터 말하자면 이는 <a href="https://itholic.github.io/python-identity-equality/" target="_blank">동일성과 동등성</a>의 차이이다.

용어를 보면 헷갈리지만,

실제로는 매우 간단한 개념이므로 그냥 예제를 보자.

```js
var a = 10
var b = '10'
```

a는 정수형 변수 10으로 선언했고,

b는 문자열 변수 '10'으로 선언했다.

이를 \== 으로 비교하면 어떻게 될까?

```js
var a = 10
var b = '10'

console.log(a == b)  // true
```

a는 정수고 b는 문자열인데 true가 나왔다.

스크립트가 실행될때, b 가 내부적으로 자동 형변환이 되기 때문이다.

그럼 \=== 비교는 어떨까?

```js
var a = 10
var b = '10'

console.log(a === b)  // false
```

false가 나왔다.

\=== 비교는 값이 "완전하게 동일한가"를 판단한다.

그러니까, 형변환을 하지 않고도 애초에 같은 객체였느냐를 판단하는 것이다.

<br/>

당연한 이야기지만 둘 중 "더 좋은것"은 없다.

만약 문자열 10과 정수 10을 같은 값으로 처리하고 싶다면 \== 비교를,

다른 값으로 처리하고 싶다면 \=== 비교를 사용하면 된다.

<br/>

\== 비교시 자동 형변환을 해주는 규칙은 너무 많아서.

본인이 자주 사용하는 규칙 몇 가지를 제외하면 암기하기보단 필요할때마다 찾아보는게 좋다.

다음 링크에 javascript에서 비교할수있는 모든 경우의수를 모아놓은 테이블이 있다.

<a href="https://dorey.github.io/JavaScript-Equality-Table/" target="_blank">JS Comparison Table</a>


<br/>

그래도 링크만 휙 던져놓고 넘어가면 매정하니까,

헷갈릴 수 있는 몇 가지만 간단히 정리해보겠다.

```js
console.log('' == 0)  // true
console.log(true == 1)  // true
console.log(true == '1')  // true
console.log(false == 0)  // true
console.log(false == '0')  // true

console.log(false == null)  // false
console.log(false == undefined)  // false
```

위의 예제에서, \== 가 아닌 \=== 일 경우는 전부다 false를 반환한다.

\=== 비교의 경우 \== 비교에 비해 직관적으로 결과를 알 수 있지만, 

다음과 같은 두 가지 상황만 조금 유의하자.

```js
console.log(0 === -0)  // true
console.log(Nan === NaN)  // false
```

0과 -0은 같은 것으로 판단한다.

NaN은 Not a Number의 약자로, 말그대로 숫자가 '아닌' 객체를 판별할때 사용한다.

NaN을 판별할 때에는 \== 도 \===도 아닌 isNaN 함수를 통해 판별해야한다.

그리고 isNaN함수 내부적으로는 \== 비교를 사용함을 유의하자.

```js
NaN == "1"  // false
isNaN("1")  // false
isNaN("hello")  // true
```

두 번째 예시를 보면, isNaN 함수가 "1"을 문자가 아닌 숫자로 판단하고있다.

"'1'은 숫자가 '아니지'?" 라는 질문에 "아니(false), 숫자야"라고 답한것이다.

참고로 != , !\== 는 똑같은 상황에서 각각 \== , === 와 정확히 반대의 결과를 출력한다.

<br/>

\== 와 \=== 를 적절히 활용하는것은 단순히 정확한 값의 비교를 위해서 뿐 아니라,

코드를 읽는 사람으로 하여금 프로그래머의 정확한 의도를 알려줄 수 있다는 측면에서도 중요하다.
