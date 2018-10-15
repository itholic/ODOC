# 인덱스

### 개념

책을 생각해보자.

인덱스는 책의 첫 장에 있는 '목차'에 주로 비유된다.

10페이지 책이 있다면 굳이 목차는 필요 없을 것이다.

물론 있어도 괜찮지만, 대부분의 사람이 목차를 활용하지 않는다면 괜한 종이 낭비가 될 수도 있다.

그럼 이번엔 10000 페이지 짜리 책이 있다고 생각해보자.

데이터베이스 서적이며, 트랜잭션에 관련된 부분을 찾아보고싶다.

10000 페이지가 어느정도인지 실감이 나지 않을 수 있는데, 다음 사진을 보자.

![10000](./img/10000page.png)
[출처 : https://blog.lib.uiowa.edu/preservation/2011/01/07/10000-page-book-bound-at-conservation-lab/]


만약 목차가 없다면 트랜잭션이 무엇인지 알아보고 싶은 마음이 눈녹듯 사라질것이다.

그런데 생각해보면.

목차가 있으면 편한건 확실하지만, 일반적인 책을 생각해보면 다음과 같이 목차가 문자열 순으로 되어있지는 않다.

```
1. Intro
2. SQL
3. DML
...
10. Transaction
11. Concurrency Control
...
50. Outro
```

문자열 순이 아닌 책의 내용 순으로, 주요 타이틀을 기준으로 목차를 만든다.

그래도 목차가 없는 것 보다는 훨씬 편리하지만, 책의 주요 내용을 가나다 순으로 정리한 목록이 있으면 내가 원하는 특정 내용 더 찾기 쉬울 것이다. 

어느정도 두꺼운 책에서는 색인이라는 것을 제공해서 바로 이러한 편의성을 제공한다. 

이 때, 색인은 영어로 Index이며, DB의 그것과 완전히 동일한 역할을 한다.


### 예시1-특정 챕터의 첫 페이지 찾기

앞서 언급한 10000 페이지짜리 데이터베이스 서적이 다음과 같이 테이블에 저장되어있다.

|page|title|
|---|---|
|1|Intro|
|2|Intro|
|3|Intro|
|...|...|
|512|SQL|
|513|SQL|
|...|...|
|5544|Optimizer|
|5545|Transaction|
|5546|Transaction|
|5547|Transaction|
|...|...|
|5700|Transaction|
|5701|Transaction|
|5702|ConcurrenctControl|
|5703|ConcurrenctControl|
|...|...|
|9999|Outro|
|10000|Outro|


Transaction 파트는 5545 페이지부터 5701 페이지 까지라는 것을 알 수 있다.

검색 방식을 쿼리로 표현하면 다음과 같다. (테이블 명은 db_book이라 하자)

```sql
SELECT	page
FROM	db_book
WHERE	title = 'Transaction';
```

말그대로 db_book이라는 테이블에서 title이 'Transaction' 이라는 page를 찾는 것이다.

해당 페이지를 찾으려면 1번 페이지부터 5545번 페이지 까지 전부 확인해보고 나서야 Transaction 파트를 찾을 수 있을 것이다.

그리고 DB 입장에서는 5545번 페이지 뿐 아니라 더 뒤쪽에도 'Transaction' 이라는 키워드가 있을 수도 있다고 생각한다.(그리고 실제로 있다)

결국 DB는 10000건의 데이터를 전체 검색하는 full scan을 수행하게 된다.

full scan은 말그대로 테이블의 전체 데이터를 몽땅 순회하는 것이다.

물론 사람의 경우라면 5545번 페이지를 찾고 검색을 중단하겠지만, 컴퓨터는 생각보다 그렇게 똑똑하지 않다.

그리고 우리가 DB에게 원하는 정보는 Transaction 파트가 시작하는 5545번 페이지일 뿐, 나머지 페이지는 필요하지 않다.

고생하는 DB를 위해 인덱스를 만들어주자. 

인덱스도 결국엔 하나의 테이블이다. index_title 이라는 이름의 테이블을 만들자.

우선 'Transaction' 이라는 키워드를 쉽게 찾을 수 있도록 abc 순으로 정렬하면 좋을 것 같다.

|title|page|
|---|---|
|ConcurrenctControl|5702|
|ConcurrenctControl|5703|
|...|...|
|Intro|1|
|Intro|2|
|Intro|3|
|...|...|
|SQL|512|
|SQL|513|
|...|...|
|Optimizer|5544|
|Outro|9999|
|Outro|10000|
|...|...|
|Transaction|5545|
|Transaction|5546|
|Transaction|5547|
|Transaction|5700|
|Transaction|5701|


편의를 위해 title컬럼과 page컬럼 의 순서를 바꾸었다.

그리고, 중복된 내용은 해당 내용의 가장 첫 번째 페이지만 남기고 전부 지워도 좋을 것 같다.


|title|page|
|---|---|
|ConcurrenctControl|5702|
|Intro|1|
|SQL|512|
|Optimizer|5544|
|Outro|9999|
|Transaction|5545|

편의상 6개의 title외에 다른 title은 없다고 가정하자.

이제 DB는 index_title 테이블에서 6개의 데이터만 찾아보면 되며, 심지어 문자열 순으로 정렬까지 되어있기 때문에 더욱 빠르게 'Transaction' 이라는 문자열을 수 있다.


### 예시2-서점에서 책 찾기


첫번째 예시는 인덱스의 필요성과 기본 동작 개념을 이해하기 위한 용도로 작성했다.

인덱스가 얼마나 드라마틱한 성능을 보이는지 설명하기 위해 편의상 인덱스 테이블에서 중복을 제거했지만, 

실제로는 인덱싱 테이블에서 중복을 제거하는 작업이 들어가지는 않는다. (물론 그렇게 사용할수도 있겠지만, 일반적인 경우를 말하는 것이다)

다음 테이블을 보자.

서점에 진열된 책들의 이름, 카테고리, 위치를 저장한 테이블이다.

10000권의 책이 있고, A~Z까지 랜덤한 위치에 진열되어있다.

|rowid|name|category|location|
|---|---|---|---|
|1|let's start java|java|A|
|2|python basic|python|K|
|3|js for seinor|javascript|B|
|4|let's start java|java|C|
|...|...|...|...|
|4222|java? java!|java|Z|
|4223|pythonic thinking|python|A|
|...|...|...|...|
|9999|javavara|java|K|
|10000|i love C++|C++|N|


어떤 java 덕후가 서점에 방문해 카테고리가 java인 책을 전부 구매하려고 한다.

카테고리가 java인 책의 이름과 위치를 전부 찾기위해 다음과 같이 쿼리했다. 

테이블명은 book_store라고 하자.

```sql
SELECT	name, location
FROM	book_store
WHERE	category = 'java'
```

결과는 다음과 같을 것이다.

|name|location|
|---|---|
|let's start java|A|
|let's start java|C|
|java? java!|Z|
|javavara|K|


현재 인덱스가 없기 때문에, 10000개의 데이터를 모두 뒤져서 결과를 찾았을 것이다.(full scan)

이번에도 불쌍한 DB를 위해 인덱스를 만들어주자.

category를 기준으로 데이터를 찾고있기 때문에, category를 기준으로 정렬해주자.

그리고 DB가 쉽게 찾아갈 수 있도록 rowid를 같이 넣어주자.

(다른 컬럼까지 모두 인덱스에 넣어버리면 결국 원본 테이블과 내용이 똑같아져 공간 낭비이므로, rowid만 넣어주는 것이다.

책의 목차에도 제목과 페이지수만 적혀있을뿐, 전체 내용이 적혀있지는 않듯이)


|category|id|
|---|---|
|...|...|
|C++|10000|
|...|...|
|java|1|
|java|4|
|java|4222|
|java|9999|
|javascript|3|
|...|...|
|python|2|
|python|4223|
|...|...|


인덱스는 문자열 순서대로 정렬되어있기 때문에,

'java' 라는 문자열을 계속 검색하다가 'javascript' 라는 문자열을 만나는 순간 이제 더이상 'java' 라는 문자열을 존재하지 않는다고 단정짓고 탐색을 종료할 수 있다.

게다가 내부적으로 데이터를 B-Tree라는 구조에 저장하기 때문에, 'java'라는 문자열을 찾아낼 때 맨 처음부터 순차적으로 조회하는 것 보다 훨씬 빠르다.

(B-Tree 관련 내용은 문서를 따로 정리할 예정)

그리고 찾아낸 rowid값을 기준으로 데이터베이스에 조회하면 그만이다.

인덱스에서 찾아낸 rowid값은 1, 4, 4222, 9999 이므로 다음과 같이 검색하면 된다.



```sql
SELECT	name, location
FROM	book_store
WHERE	rowid IN (1, 4, 4222, 9999)
```

book_store 테이블에서 rowid가 1, 4, 4222, 9999 인 책의 이름과 위치를 조회하는 쿼리이다.

**이 때, catrgory = 'java' 로 검색하는 것과 무슨 차이가 있을까 하는 의문이 생길 수 있다.**

rowid는 사실 데이터를 삽입할 때 DB 내부에서 자동적으로 생성하는 값으로, 해당 row(행)의 고유한 주소 값을 가리킨다.

따라서, rowid가 주어지면 DB는 해당 데이터의 위치가 어디있는지 일일이 찾지 않아도 rowid를 통해 바로 접근할 수 있다.

너무 자세히 들어가면 복잡해지므로, 어쨌든 이 rowid를 통한 검색은 **DB에서 가장 빠르게 데이터를 찾아낼 수 있는 검색 방법**이라는 사실을 알고있으면 된다.

즉, 인덱스를 만드는 이유는 바로 이 rowid를 기준으로 데이터를 탐색할 수 있도록 유도해서 쿼리의 성능을 향상시키기 위함이다.

실제 사용시에는 이러한 일련의 과정을 사용자가 직접 입력할 필요 없이 다음과 같이 인덱스를 생성해 놓으면 내부적으로 알아서 작동한다.

```sql
CREATE INDEX index_category ON book_store(category)
```

위와 같이 book_store 테이블의 category 컬럼에 index_category라는 인덱스를 생성한 후, 기존과 똑같이 사용하면 된다.

```sql
SELECT	name, location
FROM	book_store
WHERE	category = 'java'
```

