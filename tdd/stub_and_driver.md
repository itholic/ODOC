# 스텁 & 드라이버

1. 소프트웨어는 여러개의 클래스와 함수, 패키지들이 맞물려서 돌아간다.

2. 근데 이 모두를 전부 개발하지 않고, 일부만 개발된 상태로 기능 테스트를 해보고 싶을 수 있다.

3. 이 때, 아직 미개발된 항목들에 대해 가장 기본적인 뼈대 기능만 만들어서 단순한 기능 테스트를 할 수 있다.

4. 이 때 사용되는 개념이 스텁과 드라이버이다. 


**굳이 두 용어를 명확하게 나눠서 외울 필요는 없고, 이런 테스트 방식을 이해하는 것 자체가 핵심이다**


## 스텁

하향식 테스트, 상위 모듈에서 하위 모듈로의 테스트를 진행하는 것

- 서버-클라이언트 구조에서 서버만 구현된 상태로 테스트를 해보고 싶을수 있다.
- 이때, 단순히 값만 넘겨주는(뼈대만 있는) 가상의 클라이언트를 만들어서 테스트 할 수 있다.
- 이 가상의 클라이언트가 바로 스텁이다.

## 드라이버


상향식 테스트, 하위 모듈에서 상위 모듈로의 테스트를 진행하는 것

- 마찬가지로 서버-클라이언트 구조에서 이번엔 클라이언트만 구현된 상태로 테스트를 해보고 싶다.
- 접속 인증 등의 간단한 기능만 하는(뼈대만 있는) 가상의 서버를 만들어서 테스트 할 수 있다.
- 이 가상의 서버가 바로 드라이버이다.

