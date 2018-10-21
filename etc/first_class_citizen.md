# 일급 객체(first class citizen)

### 거두절미하고, 다음의 특징을 모두 만족하면 일급 객체이다.

1. 변수에 할당 가능하다.
2. 함수의 인자로 넘길 수 있다.
3. 함수의 리턴 값으로 반환 가능하다.

- 용어가 생소할뿐, int나 string처럼 일반적으로 변수에 할당하고, 함수의 인자 값으로 넘기거나 리턴 값으로 받는 객체들은 모두 일급 객체였던 것이다.
- 근데, 일부 언어에서는 함수도 일급 객체로 취급한다.
- 무슨말이냐고?

### JAVA
```java
public class first_class_test {
	public static void test(){
    	System.out.println("first_class_test");
    }

	public static void main(String[] args) {
    	Object a = test; // 이런거 안 됨, Syntax Error
    }

}
```
- 함수를 변수에 할당할 수 없다.
- 즉, JAVA에서의 함수는 일급 객체가 아니다.

### PYTHON
```python
def test():
	print("first_class_test")

a = test  # 변수 a에 test 함수 할당
test()  # 함수 실행, "first_class_test" 출력
```

- 함수를 변수에 할당 가능하다.
- 즉, Python에서의 함수는 일급 객체이다.
- 근데, 일급 객체는 함수의 인자로 넘기거나 리턴 값으로 반환도 가능하다고 했는데, 가능할까?


```python
def test(func):
    func = func
    return func

def adder(a, b):
    return a+b

a = test(adder)  # a 변수에 adder 함수를 건네주고, 다시 리턴
print(a(2, 3))  # 5 출력
```

- 보다시피 가능하다.
- 파이썬은 이러한 특징을 통해 클로저나 데코레이터등 유용한 기능을 제공함으로써 더욱 아름다운 프로그래밍을 가능하도록 해준다.
- 반복되는 기능을 쉽게 재사용 가능하도록 해준다는데, 대략적인 개념은 이해가 되지만 아직 더 많은 공부가 필요할듯.
