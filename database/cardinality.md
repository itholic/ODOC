# cardinality

카디널리티는 전체 행에 대한 해당 컬럼의 중복 수치를 나타내는 지표이다.

중복도가 '낮으면' 카디널리티가 '높다'고 표현한다.

중복도가 '높으면' 카디널리티가 '낮다'고 표현한다.

예를들면

|id|name|location|
|---|---|---|
|0|lee|seoul|
|1|park|pusan|
|2|choi|seoul|
|3|park|seoul|
|4|kim|seoul|
|5|bae|incheon|
|6|ahn|seoul|
|7|lee|seoul|
|8|lee|seoul|
|9|kim|seoul|

위와 같은 테이블이 있을때,

id의 경우 전체 10건의 로우에대해 중복된 값이 없으므로 카디널리티가 '높다'.

name의 경우 distinct한 값이 6건이므로 (lee, park, choi, kim, bae, ahm) 'id컬럼보다는 카디널리티가 낮다'.

location의 경우 distinct한 값이 3건밖에 없으므로 (seoul, pusan, incheon) 카디널리티가 '제일 낮다'.

즉, 카디널리티는 객관적 수치보다는 상대적인 개념으로 이해해야한다.

인덱스를 걸 때, 내가 원하는 데이터를 선택하는 과정에서 최대한 많은 데이터가 걸러져야 성능이 좋을것이다.

(선택하는 데이터가 많아질수록 full scan에 가까워지므로)

즉, 여러 컬럼을 동시에 인덱싱할때, 다음과 같이 카디널리티가 높은 컬럼을(중복이 적은 컬럼을) 우선순위로 두는 것이 인덱싱 전략에 유리하다.

```sql
CREATE INDEX idx_localtion_first ON users(location, name, id)
CREATE INDEX idx_id_first ON users(id, name, location)

-- * 옵티마이저가 인덱스를 자동선택하지 못하게 use index를 통한 강제 인덱싱으로 쿼리 테스트

-- 1. idx_location_first

SELECT    *
FROM      users
use index (idx_location_first)
WHERE     id = '0'
AND       name = 'lee'
AND       location = 'seoul';
-- 먼저, 인덱스에서 location이 'seoul'인 값을 거르므로, 해당하는 8개의 데이터가 남음
-- 다음, name이 'lee'인 데이터를 거르기 위해 남은 8개 데이터의 정합성을 확인해서 일치하는 3개 데이터가 남음
-- 마지막으로, id가 '0'인 값을 거르기 위해 남은 3개 데이터의 정합성을 확인함


-- 2. idx_id_first

SELECT    *
FROM      users
use index (idx_id_first)
WHERE     id = '0'
AND       name = 'lee'
AND       location = 'seoul';
-- 먼저, 인덱스에서 id = '0'인 값을 거르므로 단 한건의 데이터만 남음
-- 다음, 인덱스에서 남은 한 건의 데이터에 대해서만 name = 'lee'인지 정합성을 확인함
-- 마지막으로, 역시 남은 한 건의 데이터에 대해서만 location = 'seoul'인지 정합성을 확인함
```

예시에서는 데이터 갯수가 작아 체감이 안되겠지만,

수천, 수만, 나아가 수십 수백만 개의 데이터에 대한 인덱싱에서는 현저한 성능차이를 보인다.

따라서 인덱싱 컬럼을 선택시, 카디널리티에 대한 고려는 매우 중요하다고 할 수 있다.

