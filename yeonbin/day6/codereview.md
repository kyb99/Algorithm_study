# 230816
## 수열
### 현기
- sum을 빼고 풀었다
```python
result = []
K = 3
N = 10 # 0~9
degrees = [2, 2, 1, 2, 4, 5]
result = []
처음에 result.append(sum(degrees[:K])) #(0 ~ K-1 까지 합)
# result = [5, 5, 7, ...]  # 앞으로 이런식으로 append됨
# 우리가 구하고 싶은건 K (1~K) ~... N-1 (N-K ~ N-1)까지 만큼 
for i in range(N-K):#  N-K 개
 result.append(result[i] - temp[i] +temp[K+i])

 ```
### 승집
- while
```python
while i != N-M:
# 제일앞에 잇는거 빼고 가장 가까운 애 넣는다
```
### 흔오
- append 안씀

## 2491 수열
- 조건을 똑바로 보자
### 현기
- 길이 최소는 1이니까 1부터 시작, 증가, 감소 값 따로
- 연속 증가, 연속 감소 따로 for문 돌렸다
### 승집
- while문 사용
- 업, 다운 한번에 처리
- 처리 순서가 중요
  - == 를 먼저해주고(up+1, down+1), 나머지 두개 해주기
  - up: up+1, max 비교하고, down = 1
  - 마지막에 남은거까지 비교해줘야함!
### 현오
- 현기오빠랑 같음
- 실수한거
  - 방향이 바뀔때만 max갱신 > 끝까지면 갱신 반영 못함

