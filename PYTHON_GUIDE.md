
# Python

```python
round(number, round_index) # round_index가 자리수, 인자가 없으면 소수점 첫번째 자리에서 반올림
number // number # 을 이용해서 몫만 구할 수 있음
number ** number # 제곱
val.append() # 붙이기
val.remove(특정 값(옵션)) # 제거하기
val = list() # 리스트 선언하는 방법
val = [] # 리스트 선언하는 방법
val = [0] * 10 # 크기 10인 초기값이 0인 리스트
val[numberA : numberB] # numberA 인덱스부터 numberB-1 인덱스까지
array = [i for i in range(20) if i % 2 == 1] # 1,3...
range(number) # 0부터 number -1까지, 항상 마지막 숫자는 제외
array = [[0] * 4 for _ in range(5)] # 4 x 5 리스트 0으로 초기화
array = [[0] * 4] * 5 # 위와 동일 -> 사용 안하는게 좋음
# 2차원 리스트를 초기화할 때는 반드시 리스트 컴프리헨션을 이용해야함, 참조가 걸려있는 듯
val.sort(reverse = True) # 정렬
val.reverse() # 순서 뒤집기
insert(삽일할 위치 인덱스 삽입 할 값) # 특정 인덱스에 원소 삽입
val.count(특정 값(옵션)) # 특정 값의 개수
```

#### 딕셔너리

```python
data = dict() # 해시 테이블을 이용한 사전 자료형
data.keys() # 키 값만 뽑을 수 있음
data.values() # 벨류 값만 뽑을 수 있음
```

#### 문자열

```python
문자열 * 3 # 이게 성립이 됨
문자열[2:4] # 인덱스 2부터 4-1 까지 출력
```

#### Set

> 시간 복잡도 O(1)

```python
data.set(리스트) # 집합
data = {1,1,2,3,4} # 이것도 집합으로 중복 제거됨
| # 합집합, 집합 자료형의 연산임
& # 교집합
- # 차집합
data.update(리스트) # 여러개를 한꺼번에 추가 가능
data.add(값) # 새로운 원소 추가
data.remove(값) # 원소 제거
```

```python
a = [1,2,3,4,5,6]
remove_set = {1,4}
result = [i for i in a if i not in remove_set] # 1,2,3,4
```

#### 조건문

```python
if, elif, else # 가 존재함
and, or, not # 도 존재함
in 연산자, not in 연산자 # 도 존재함
X in 리스트
X not in 문자열
"A" if scoure >= 80 else "B" # 조건부 표현식
```

#### 반복문

```python
while 조건:
for 변수 in 리스트:
continue
```

#### 함수

```python
def 함수명(매개변수):
return
# 함수 외부에 있는 값에 접근하려면 global을 이용
```

#### 입출력

```python
int() # 정수로 바꾸기
split() # 분리 가능
map() # 맵으로 만들기
list(map(int, input().split())) # 중요!
n = int(input()) # 데이터의 개수 입력
data = list(map(int, input().split())) # 이건 여러개 공백으로 된 줄 입력
a,b,c = map(int, input().split()) # 이렇게 나눠서 값이 들어가게 할 수도 있음

# 입력 또 다른 방법 -> 성능상
import sys
sys.stdin.readline().rstrip() # 마지막 함수는 공백 문자를 제거

str(변수) # 문자열로 바꾸기

# 3.6이상
f"문자열 ~ {변수}" # 자바스크립트 백틱과 비슷함
```

#### 라이브러리

내장

```python
sum()
min()
sorted() # 이터레이터 객체가 들어왔을 때, 정렬된 결과를 반환
```

itertools

```python
permutations
combinations
product
comninations_with_replacement
```

heapq

```python
heapq.heappush(key, value)
heapq.heappop(key)
max힙은 값을 -로 집어넣기, 뺄때도 -를 붙여줘야됨
```

bisect : 이진 탐색 기능

```python
bisect_left
bisect_right
```

collections : 덱, 카운터 등

```python
data = deque
data.appendList(value)
data.append(value)
Counter : 해당 값이 몇번 등장하는지 출력해줌
dict로 사전 자료형으로 변환도 가능함
```

math

```python
factorial(value)
sqrt(value) : 제곱근
gcd(a,b) : 최대공약수
pi : 파이
e : 자연상수
```